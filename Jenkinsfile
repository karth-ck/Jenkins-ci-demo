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
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'python3 -m pytest test_app.py'
      }
    }
  }
}

