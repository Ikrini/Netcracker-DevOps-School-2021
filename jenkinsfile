pipeline {
  environment {
    imagename = "gcr.io/netcracker-devops/telebot34"
    registryCredential = 'my-project-gcr-credentials'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'git@github.com:Ikrini/Netcracker-DevOps-school-2021.git'

      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename ":$BUILD_NUMBER" 
        }
      }
    }
  }
}
