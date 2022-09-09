ansiColor('xterm') {
    node {
        stage('Checkout') {
            // Clean the workspace
            cleanWs()
            // Get some code from a GitHub repository
            checkout scm
        }
        stage('Setup') {
           // sh "ansible-galaxy install -r requirements.yml"
            sh 'echo "setup placeholder"'
        }
        stage('Validate') {
            sh "packer validate base_docker.json"
        }
        stage('Build') {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws_sunny', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
            // Run the packer build
            sh "packer build base_docker.json"
            }
        }
        stage('Store Artifacts') {
            archiveArtifacts 'manifest.json'
        }
    }
}
