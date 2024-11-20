pipeline {
    agent any 

    parameters {
        choice(name: 'TRANSFORMATIONS', choices: ['remove_duplicates', 'remove_nulls', 'last_position'], description: 'Escolha as transformações')
        string(name: 'NULL_COLUMNS', defaultValue: '', description: 'Colunas para remover nulos (separadas por vírgula)')
        string(name: 'ORDER_BY', defaultValue: '', description: 'Coluna para ordenar (última posição)')
        string(name: 'PARTITION_BY', defaultValue: '', description: 'Coluna para partição (última posição)')
        string(name: 'FILE', defaultValue: '', description: 'Caminho do arquivo CSV a ser processado')
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                // Clona o repositório Git
                git 'https://github.com/seu_usuario/seu_repositorio.git'
            }
        }
        stage('Preparar Ambiente') {
            steps {
                script {
                    // Instala dependências
                    sh 'pip install -r jenkins/requirements.txt'
                }
            }
        }
        stage('Executar ETL') {
            steps {
                script {
                    // Executar os scripts Python na pasta jenkins
                    sh "python jenkins/extract.py ${params.FILE}"
                    sh "python jenkins/transform.py --transformations='${params.TRANSFORMATIONS}' --null_columns='${params.NULL_COLUMNS}' --order_by='${params.ORDER_BY}' --partition_by='${params.PARTITION_BY}'"
                    sh 'python jenkins/load.py'
                }
            }
        }
    }
    post {
        success {
            echo 'ETL executado com sucesso!'
        }
        failure {
            echo 'Falha na execução do ETL.'
        }
    }
}