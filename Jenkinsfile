pipeline {
    agent any
    stages {
        stage('Docker Version') {
            steps {
                script {
                    docker.image('docker:19.03.12').inside('--privileged') {
                        sh 'docker version'
                    }
                }
            }
        }
    }
}
