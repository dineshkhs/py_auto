def PYTHON_VERSION = '3.11'


def ALPINE_VERSION = '3.17'

pipeline {
  agent {
        docker { image "python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}"
       }
  }
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
