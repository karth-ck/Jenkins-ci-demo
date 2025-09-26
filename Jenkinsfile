pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Install Python & Pip (if needed)') {
            steps {
                // Check if python3 exists
                sh '''
                if ! command -v python3 >/dev/null 2>&1; then
                    echo "Python3 not found. Installing..."
                    sudo yum install -y python3 || sudo apt install -y python3
                fi

                # Check if pip3 exists
                if ! python3 -m pip --version >/dev/null 2>&1; then
                    echo "pip3 not found. Installing..."
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python3 get-pip.py --user
                    export PATH=$PATH:~/.local/bin
                fi
                '''
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
    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
