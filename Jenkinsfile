pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker build -t karimaraby/devops-journey:backflask-5.${env.BUILD_NUMBER} backend-flask/"
                sh "docker build -t karimaraby/devops-journey:frontapi-4.${env.BUILD_NUMBER} frontend-html/"
                sh "docker build -t karimaraby/devops-journey:front-1.${env.BUILD_NUMBER} frontend-html/templates/"

            }
        }
    }
}