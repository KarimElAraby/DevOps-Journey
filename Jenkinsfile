pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker version"
                sh "kubectl kubectl version"

            }
        }
    }
}