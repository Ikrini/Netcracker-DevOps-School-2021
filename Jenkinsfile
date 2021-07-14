pipeline {
  environment {
    imagename          = "gcr.io/netcracker-devops/telebot"
    imagenamek         = "gcr.io/netcracker-devops/telekuber"   
    registryCredential = 'my-project-gcr-credentials'
    ConfigPy           =  credentials('config.py')
    Config_k8sPy       =  credentials('config_k8s.py') 
    dockerImage        = ''
    dockerImagek       = ''
    project_name       = "test_telebot"
  }

  agent any 

  stages {
  
    stage('Building image') {
       steps {
         script {
             sh '''
                pwd
                whoami
                ls -la
                 
                '''
                 withCredentials([file(credentialsId: 'config.py', variable: 'FILE')]) {
                   
                     dir("code") {  
                                   dockerImage  = docker.build imagename  + ":$BUILD_NUMBER" 
                     }

                     dir("code-kuber") {
                                         sh "ls -la"
                                         dockerImagek = docker.build imagenamek + ":$BUILD_NUMBER"
                     }
                 }
        }
      }
    }

    stage('Build Test') {
        steps {
            echo "Start of Stage Test"
            echo "Project name is ${project_name}"
            echo "end of Stage Test"
            sh "pwd"
            sh "ls -la"
        }
    }
    
    stage('Continuous Delivery image to GCR') {
        steps {
            script {
               docker.withRegistry( 'https://gcr.io', 'gcr:my-project-gcr-credentials') {
 
                      dockerImage.push("$BUILD_NUMBER")
                      dockerImage.push('latest')
                      dockerImagek.push('latest')
            }
         }
     }
   }
   
   stage('Continuous Deploy / docker-compose') {
       steps {
           script {
                        
                   sh "pwd" 
                   sh "ls"

              withCredentials([file(credentialsId: 'config.py', variable: 'FILE')]) {

                       sh "./checker.sh"               
                 
                    dir("code") {

                         sh '''
                         pwd
                         ls -la
                         echo ${WORKSPACE}                                 
                         docker-compose stop
                         docker-compose down && docker-compose up -d     
                         pwd                
                            '''

                }
              }
           }
       }
   }
   
   stage('Prod Test') {
        steps {
            echo "Start of Stage Test"
            echo "Project name is ${project_name}"

            dir("code") {
              
                 sh "python3 ./tests.py"
//               sh "./tests.py"          

            }
 
            dir("code-kuber") {

                 sh "python3 ./tests.py"
//               sh "./tests.py"

            }

                echo "end of Stage Test"
                sh "pwd"
                sh "ls -la"
        }
    }

   stage('Push Notification') {
     steps {  
       script{
              withCredentials([string(credentialsId: 'telegramToken', variable: 'TOKEN'),
               string(credentialsId: 'telegramChatId', variable: 'TelegramChatId')]) {
                sh ”””
                   cat ${TOKEN}
                   curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=”HTML” -d text=”<b>Project</b> :
                   POC \
                  <b>Branch</b>: master \
                  <b>Build </b> : OK \
                  <b>Test suite</b> = Passed”
                   ”””
             }
       }
     }
   }
   
  //   stage('Push Notification') {
  //     steps {
  //         script{
  //                 withCredentials([string(credentialsId: 'telegramToken', variable: 'TOKEN'),
  //                          string(credentialsId: 'TelegramChatId', variable: 'CHAT_ID')]) {
  //                      
  //                            post { 
  //                             always{     
  //                                 telegramSend(message:'${PROJECT_NAME}:${BUILD_STATUS}',chatId:${CHAT_ID})
  //                             }
  //                            }  
  //                }
  //        } 
  //     } 
  //  }


   stage('Continuous Deploy to K8s / Apply  Kubernetes files') {
       steps {
            script {     
 
               withCredentials([file(credentialsId: 'config_k8s.py', variable: 'FILE')]) {                     
                
                  withKubeConfig([credentialsId: 'netcracker-devops', serverUrl: 'https://35.193.165.173']) {

                  sh ''' 
                         ./checker_k8s.sh
                           
                         kubectl get svc
                         kubectl get deploy
                         kubectl get pods
                         kubectl apply -f deployment.yaml
                         kubectl get svc
                         kubectl get deploy
                         kubectl get pods
                         
                     '''
                 }
              }

        }
     }
   }
   
   
 }
}
