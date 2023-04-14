pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh "chmod +x -R ${env.WORKSPACE}"
      }
    }
    stage('byte converstion') {
      steps {
        sh 'python3 byteconvertion.py'
      }
    }
  }
}
