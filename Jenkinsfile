pipeline {
   agent { docker { image 'python:3.6' } }

   stages {
        stage('Build environment') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install -r requirements.txt --user'
                }
            }
        }       
        stage('Test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                  withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                     sh 'python -m pytest --variables variabes.yaml test_cf_ota.py'
                 }
                }
        }
      }
   }
}
