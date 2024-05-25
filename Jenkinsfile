pipeline {
    agent {

    stages {
        stage('Build') {
            steps {
                container('docker') {
                    sh 'docker version'
                    }
                }
            }
        }
    }
}
