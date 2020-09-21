pipeline {
   agent { docker { image 'python:3.7.2' } }

   stages {
        stage('Build environment') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }       
        stage('Test') {
            steps {
                sh 'python -m pytest  --variables variabes.yaml test_cf_ota.py'
        }
      }
   }
}
