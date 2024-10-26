Sistema de ETL de arquivos, primeiramente fazer ETL de arquivos CSV e JSON, podendo ler um ou varios arquivos do mesmo tipo e criando a tabela.

Funcoes do Sistema
- ~~Criar tabelas de arquivos json e csv~~
- ~~carregar um ou varios arquivos csv ou json~~
- ~~implementar opcao de filtros por query externa~~
- ~~remover dados duplicados~~
- ~~pegar o registro mais atualizado~~
- ~~usar openia para a selecao das colunas~~
-- -
To do
- criar frontend
- criar opcao de upload de arquivo
- devolver o arquivo no front para download
- adicionar os filtros no frontend, opces que o usuario vai querer fazer de tratamento nos dados
- criar frontend possivel de fazer upload de um arquivo, ele pegar o arquivo, fazer a criacao da tabela, e jogar de volta para usuario fazer download

Para definir variavel de ambiente no Windows, utilizar os comando abaixo no terminal

    setx OPENAI_API_KEY "your_api_key_here"

No Linux

    export OPENAI_API_KEY="your_api_key_here"