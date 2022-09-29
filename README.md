# sitechecker

## Ambiente Linux (Ou WSL)

- Faça o clone do projeto, e entre na pasta como no exemplo:

    `cd /home/hugosousa111/lighthouse/sitechecker/`
    
- Obs: Sempre que nesse tutorial aparecer o caminho `/home/hugosousa111/lighthouse/sitechecker/` ele deve ser trocado pelo caminho do projeto no seu computador, aqui é usado apenas como exemplo

- Crie um ambiente virtual, com o seguinte comando: 

    `python -m venv venv`
    
- Ative o ambiente virtual:

    `source venv/bin/activate`     

- Altere a linha 9 do arquivo `sitechecker/__main__.py` para o caminho do projeto do seu computador, esse caminho é utilizado para salvar o arquivo de logs do sistema (`sitechecker.log`)

    `PATH_PROJECT = '/home/hugosousa111/lighthouse/sitechecker/'`
    
- Todos os pacotes utilizados nesse projeto já vem pré-instalados no python, sendo opcional instalar: 
    
    `pip install -r requirements.txt`
    
## Rodando o sistema

- O sistema pode ser utilizado de duas maneiras:

    - Passando os sites por parâmetro: 
    
        `python -m sitechecker --urls globo.com indicium.tech`
        
    - Passando os sites por parâmetro através de um arquivo csv: 
    
        `python -m sitechecker --file file_urls.csv`
        
        - O arquivo `file_urls.csv` é um exemplo do formato ideal para esse sistema, um csv de uma coluna ("sites"), separados por quebra de linha
        
### Utilizando o CRON

- Para utilizar o agendador de tarefas CRON do Linux deve-se: 

- Altere a linha 9 do arquivo `sitechecker/__main__.py` para o caminho do projeto do seu computador, esse caminho é utilizado para salvar o arquivo de logs do sistema (`sitechecker.log`)

    `PATH_PROJECT = '/home/hugosousa111/lighthouse/sitechecker/'`
    
- No arquivo `site_checker.sh`, altere a linha 2 para o caminho do projeto do seu computador: 
    
    `cd /home/hugosousa111/lighthouse/sitechecker/`
    
- É recomendado alterar as permissões do seu arquivo `sitechecker.sh`

    `chmod 777 sitechecker.sh`
    
- Garanta que o serviço cron está rodando (Principalmente se utilizar WSL): 

    `sudo service cron start`
    
- Inicie o processo de escrita do arquivo cron, com o comando: 

    `crontab -e` 
    
    - Se for a primeira vez rodando o sistema, escolha um editor de texto no terminal
    
- No arquivo, vamos escrever a periodicidade que o comando vai ser escutado, o que queremos que seja executado, e para onde vai as saídas do sistema. Nesse caso, vai ser executado o arquivo `sitechecker.sh`, de minuto em minuto, e as saídas são colocadas em `output.log`, lembre-se de alterar os caminhos para o do projeto no seu computador: 

    `* * * * * /home/hugosousa111/lighthouse/sitechecker/sitechecker.sh >> /home/hugosousa111/lighthouse/sitechecker/output.log 2>&1`
    
    - Para outros exemplos de formato de tempo de execução, acesse: https://crontab.guru/
    
- Para observar o arquivo cron: 

    `crontab -l`
    
- Você pode observar os logs do cron através do comando

    `grep -i cron /var/log/syslog`
    
- Você também pode alterar os parâmetros no arquivo `sitechecker.sh`, para testar outros sites ou arquivos
