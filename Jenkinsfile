pipeline {
    agent any 

    parameters {
        choice(name: 'TRANSFORMATIONS', choices: ['remove_duplicates', 'remove_nulls', 'last_position'], description: 'Escolha as transformações')
        string(name: 'NULL_COLUMNS', defaultValue: '', description: 'Colunas para remover nulos (separadas por vírgula)')
        string(name: 'ORDER_BY', defaultValue: '', description: 'Coluna para ordenar (última posição)')
        string(name: 'PARTITION_BY', defaultValue: '', description: 'Coluna para partição (última posição)')
    }

    stages {
        stage('Preparar Ambiente') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Executar ETL') {
            steps {
                script {
                    // Carregar dados
                    def extractor = new Extract()
                    def df = extractor.web_one_input_csv(params.FILE) // Supondo que FILE seja um parâmetro de entrada

                    // Aplicar transformações
                    def transformer = new Transform(df)
                    def options = [:]
                    
                    if (params.TRANSFORMATIONS.contains('remove_nulls')) {
                        options['remove_nulls'] = true
                        options['null_columns'] = params.NULL_COLUMNS.split(',')
                    }
                    if (params.TRANSFORMATIONS.contains('remove_duplicates')) {
                        options['remove_duplicates'] = true
                    }
                    if (params.TRANSFORMATIONS.contains('last_position')) {
                        options['last_position'] = true
                        options['order_by'] = params.ORDER_BY
                        options['partition_by'] = params.PARTITION_BY
                    }

                    df = transformer.apply_transformations(options)

                    // Salvar dados
                    def loader = new Load(df)
                    loader.save_parquet_table('output_file')
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