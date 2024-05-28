pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker build -t karimaraby/devops-journey:backflask-5.${env.BUILD_NUMBER} backend-flask/"
                sh "docker build -t karimaraby/devops-journey:frontapi-4.${env.BUILD_NUMBER} frontend-html/"
                sh "docker build -t karimaraby/devops-journey:front-1.${env.BUILD_NUMBER} frontend-html/templates/"
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-cred', 
                        usernameVariable: 'USER', 
                        passwordVariable: 'PASS'
                        )]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push karimaraby/devops-journey:backflask-5.${env.BUILD_NUMBER}"
                    sh "docker push karimaraby/devops-journey:frontapi-4.${env.BUILD_NUMBER}"
                    sh "docker push karimaraby/devops-journey:front-1.${env.BUILD_NUMBER}"
                }
            }
        }
    stage('test') {
            steps {
                sh "echo 'Testing....'"
                sh "echo 'Some testing scripts'"
            }
        } 
    stage('deploy') {
            steps {
                sh "kubectl set image deployment/deployment-front -n=default front-static=karimaraby/devops-journey:backflask-5.${env.BUILD_NUMBER}"
                sh "kubectl set image deployment/deployment-front -n=default front-static=karimaraby/devops-journey:frontapi-4.${env.BUILD_NUMBER}"
                sh "kubectl set image deployment/deployment-front -n=default front-static=karimaraby/devops-journey:front-1.${env.BUILD_NUMBER}"
            }
        }
    }
}