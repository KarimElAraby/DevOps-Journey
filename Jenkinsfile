pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker build -t karimaraby/devops:back-7.${env.BUILD_NUMBER} backend-flask/"
                sh "docker build -t karimaraby/devops:front-6.${env.BUILD_NUMBER} frontend-html/"
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-cred', 
                        usernameVariable: 'USER', 
                        passwordVariable: 'PASS'
                        )]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push karimaraby/devops:back-7.${env.BUILD_NUMBER}"
                    sh "docker push karimaraby/devops:front-6.${env.BUILD_NUMBER}"
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
                sh "echo 'Deploying....'"
                sh "kubectl set image deployment/backend -n=default backend=karimaraby/devops:back-7.${env.BUILD_NUMBER}"
                sh "kubectl set image deployment/frontend -n=default frontend=karimaraby/devops:front-6.${env.BUILD_NUMBER}"
            }
        }
    }
}