pipeline {
  environment {
    imagename          = "gcr.io/netcracker-devops/telebot"
//    imagenamek         = "gcr.io/netcracker-devops/telekuber"   
    registryCredential = 'my-project-gcr-credentials'
    ConfigPy           =  credentials('config.py')
    Config_k8sPy       =  credentials('config_k8s.py') 
    dockerImage        = ''
//   dockerImagek       = ''
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
//                withCredentials([file(credentialsId: 'config.py', variable: 'FILE')]) {
                   
                     dir("code") {  
       
//                     sh "cp ${ConfigPy}  /var/lib/jenkins/workspace/test_telebot/code"    # this is not solution.
                     dockerImage  = docker.build imagename + ":$BUILD_NUMBER"
//                     dockerImagek = docker.build imagenamek + ":$BUILD_NUMBER" 
                     }
//                }
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
//                dockerImagek.push('latest')
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

//                def filePath = "/var/lib/jankins/workspace/test_telebot/"

//                   sh "./checker.sh"               
                 
                dir("code") {

                   sh '''
                         pwd
                         ls -la
                         echo ${WORKSPACE}
#                         cp ${ConfigPy} /var/lib/jenkins/workspace/test_telebot/
                         docker ps -a
#                         docker container stop configpy 
#                         docker rm configpy    
#                         docker run -d -v /var/lib/jenkins/config.py:/usr/src/app/config.py --name configpy  gcr.io/netcracker-devops/telebot                         
#                         docker run --mount type=volume,source=configpy,destination=/usr/src/app                                 

                         docker-compose stop
                         docker-compose down && docker-compose up -d     
                         pwd                
                      '''
//                   env.IS_NEW_VERSION = sh (returnStdout: true, script: "[ '${env.DEPLOY_VERSION}' ] && echo 'YES'").trim()
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
              
//                 sh "python3 ./tests.py"
//               sh "./tests.py"          

            }

//            sh /var/lib/jenkins/workspace/test_telebot/code/tests.sh
            echo "end of Stage Test"
            sh "pwd"
            sh "ls -la"
        }
    }
   
   stage('Continuous Deploy to K8s / Apply  Kubernetes files') {
       steps {
            script {     
 
               withCredentials([file(credentialsId: 'config_k8s.py', variable: 'FILE')]) {                     
                
                  withKubeConfig([credentialsId: 'netcracker-devops', serverUrl: 'https://35.193.165.173']) {

                  sh ''' 
                         ./checker_k8s.sh
                           
                         kubectl get svc
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
