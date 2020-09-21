pipeline {
   agent { docker { image 'python:3.7.2' } }

   stages {
        stage('Build environment') {
            steps {
                sh 'pip --no-cache-dir install -r requirements.txt'
            }
        }       
        stage('Test') {
            steps {
                sh 'python -m pytest  --variables variabes.yaml test_cf_ota.py'
        }
      }
   }
}
