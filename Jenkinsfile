pipeline {
  agent any
  stages {
    stage('stage 1') {
      steps {
        sh 'python --version'
        sh 'java --version'
        sh 'echo salut tout le monde'
      }
    }
    stage('stage 2') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}