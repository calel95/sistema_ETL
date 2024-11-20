pipeline {
    agent any 
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/calel95/sistema_de_rifa.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        // stage('Create Item') {
        //     steps {
        //         script {
        //             def response = httpRequest(
        //                 url: 'http://localhost:8000/numeros/',
        //                 httpMode: 'POST',
        //                 contentType: 'APPLICATION_JSON',
        //                 requestBody: '{"name": "Item1", "price": 100}'
        //             )
        //             echo "Response: ${response.content}"
        //         }
        //     }
        // }
        stage('Read Item') {
            steps {
                script {
                    def response = httpRequest(
                        url: 'http://localhost:8000/numeros/',
                        httpMode: 'GET'
                    )
                    echo "Response: ${response.content}"
                }
            }
        }
        stage('Update Item') {
            steps {
                script {
                    def response = httpRequest(
                        url: 'http://localhost:8000/numeros/14',
                        httpMode: 'PUT',
                        contentType: 'APPLICATION_JSON',
                        requestBody: '{"numero":14,"nome":"baba","created_at":"2024-11-08T00:03:12.024656Z","updated":true,"update_date":"2024-11-09T00:05:35.587714"}'
                    )
                    echo "Response: ${response.content}"
                }
            }
        }
        stage('Delete Item') {
            steps {
                script {
                    def response = httpRequest(
                        url: 'http://localhost:8000/numeros/1',
                        httpMode: 'DELETE'
                    )
                    echo "Response: ${response.content}"
                }
            }
        }
    }
}