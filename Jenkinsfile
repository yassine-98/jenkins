pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello phrase') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}
