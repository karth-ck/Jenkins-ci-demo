pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building project...'
      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'pytest test_app.py'
      }
    }
  }
}
