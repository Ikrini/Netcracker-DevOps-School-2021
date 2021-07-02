pipeline {
  environment {
    imagename = "gcr.io/netcracker-devops/telebot"
    registryCredential = 'my-project-gcr-credentials'
    dockerImage = ''
    project_name = "test_telebot"
  }
  agent any
  stages {
  
    stage('Building image') {
       steps {
         script {
             sh '''
                pwd
                ls -la
                
                '''
             dir("code") {
                 
             dockerImage = docker.build imagename + ":$BUILD_NUMBER" 
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
            }
         }
     }
   }
   
   stage('Continuous Deploy / docker-compose') {
       steps {
           script {
               dir("code") {
                   sh '''
                         pwd
                         ls -la
                         docker-compose stop
                         docker-compose down && docker-compose up -d     
                         pwd                
                      '''
//                   env.IS_NEW_VERSION = sh (returnStdout: true, script: "[ '${env.DEPLOY_VERSION}' ] && echo 'YES'").trim()
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

//            sh /var/lib/jenkins/workspace/test_telebot/code/tests.sh
            echo "end of Stage Test"
            sh "pwd"
            sh "ls -la"
        }
    }
   
   stage('Continuous Deploy to K8s / Apply  Kubernetes files') {
       steps {
            script {     
                  withKubeConfig([credentialsId: 'netcracker-devops', serverUrl: 'https://35.193.165.173']) {
                  sh ''' 
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
