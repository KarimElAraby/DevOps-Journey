pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "kubectl kubectl version"
                sh "docker version"

            }
        }
    }
}