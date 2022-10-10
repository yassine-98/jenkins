pipeline {
  agent {
    docker { image 'python:3-alpine' }
  }
  stages {
    stage('Build') {
      steps {
        sh 'python hello.py'
        sh 'env | sort'
        echo "Build id is ${currentBuild.id}"
      }
    }
  }
}
