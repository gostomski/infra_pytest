pipeline {
   agent { docker { image 'python:3.6' } }

   stages {
        stage('Build environment') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 -m pip install -r requirements.txt --user'
                }
            }
        }       
        stage('Test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m pytest  --variables variabes.yaml test_cf_ota.py'
                }
        }
      }
   }
}
