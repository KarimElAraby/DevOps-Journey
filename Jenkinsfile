pipeline {
    agent any
    stages {
        stage('Docker Version') {
            steps {
                script {
                    def dockerImage = 'docker:19.03.12'
                    sh "docker pull ${dockerImage}"
                    sh "docker run --privileged --rm ${dockerImage} docker version"
                }
            }
        }
    }
}
