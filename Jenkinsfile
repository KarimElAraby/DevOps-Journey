pipeline {
    agent {
        docker {
            image 'docker:19.03.12'
            args '--privileged' // Required to run Docker within Docker
        }
    }
    stages {
        stage('Docker Version') {
            steps {
                sh 'docker version'
            }
        }
    }
}
