pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker build -t karimaraby/devops-journey:testpiple-1.${env.BUILD_NUMBER} ."

            }
        }
    }
}