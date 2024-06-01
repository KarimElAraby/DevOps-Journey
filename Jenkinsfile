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
              sh 'echo 'Deploying....''
                sh 'sed -i 's|image: .*$|image: karimaraby/devops:back-7.${env.BUILD_NUMBER}|' manifests/back-deploy.yaml'
                sh 'sed -i 's|image: .*$|image: karimaraby/devops:front-6.${env.BUILD_NUMBER}|' manifests/fron-deploy.yaml'
            }
        }
        stage('push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'git-cred', 
                        usernameVariable: 'USER', 
                        passwordVariable: 'PASS'
                        )]) {
                            sh 'git config --global user.email "jenkins@example.com"'
                            sh 'git config --global user.name "jenkins"'
                            sh "git remote set-url origin hhtps://${USER}:${PASS}@github.com/KarimElAraby/DevOps-Journey.git"
                            sh 'git add .'
                            sh 'git commit -m "Jenkins pipeline"'
                            sh 'git push origin HEAD:master'
                        }
                    }
               }
            }
        }