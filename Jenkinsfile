pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker ps"
                sh "kubectl get pod -n default"

            }
        }
    }
}