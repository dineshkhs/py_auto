pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('byte converstion') {
      steps {
        sh 'python3 byteconvertion.py'
      }
    }
  }
}
