pipeline {
  environment {
    imagename = "gcr.io/netcracker-devops/telebot"
    registryCredential = 'my-project-gcr-credentials'
    dockerImage = ''
    project_name = "test_telebot"
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
       git([url: 'git@github.com:Ikrini/Netcracker-DevOps-school-2021.git', branch: 'master', credentialsId: 'telebot-git-ssh'])

      }
    }
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
    stage('Test') {
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
   
   stage('Continuous Deploy') {
       steps {
           script {
               dir("code") {
                   sh '''
                   pwd
                   ls -la
                   docker-compose down && docker-compose build --pull && docker-compose up -d
                   
                   
                   '''
//                   env.IS_NEW_VERSION = sh (returnStdout: true, script: "[ '${env.DEPLOY_VERSION}' ] && echo 'YES'").trim()
               }
           }
       }
   }
   
 }
}
