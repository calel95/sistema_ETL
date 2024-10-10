pipelipe {
    agent any
    stages{
        stage('version'){
            steps{
                sh 'python3 --version'
                }
            }
        stage('create_faker_date'){
            steps{
                sh 'src/main.py'
                }
            }
        }
    }