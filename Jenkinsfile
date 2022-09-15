pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
        sh 'java --version'
        sh 'echo salut tout le monde'
      }
    }
    stage('hello phrase') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}