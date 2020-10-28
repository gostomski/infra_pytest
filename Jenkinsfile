def awsCredentials = [[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 's3_access']]

node('local-docker') {
        stage('Test') {
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 's3_access', variable: 'AWS_ACCESS_KEY_ID']]) {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    docker.image('python:3.6').inside {
                        sh 'pip install -r requirements.txt --user'
                        sh "echo this is ${env.AWS_ACCESS_KEY_ID}"
                        sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-1'
                        sh 'python -m pytest --variables variabes.yaml test_cf_ota.py'
                     }                     
                 }
            }     

        }        

}


