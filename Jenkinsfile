pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
        sh 'java --version'
        sh 'ping localhost'
      }
    }
    stage('hello phrase') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}