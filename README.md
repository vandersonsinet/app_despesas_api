# Minha API

Esta aplicacao tem o objetivo de manter um cadastro de despesas.

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
python -m venv env  
```

```
/env/bin/activate
```

```
(env)$ pip install -r requirements.txt
```

Para inicializar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

Após a inicializacao do servidor, o arquivo db.sqlite3 será criado automaticamente com as duas tabelas do sistema.

Para carga inicial na tabela de tipo de despesas: 
    - finalize o servidor com o comando CTRL+C no terminal
    - execute o arquivo script_insert_tipo_despesa.py clicando com o botão direito do mouse e utilizando a opçao “Executar arquivo do Python no terminal”

Certifique que a tabela tipo_despesa esteja devidamente populada no arquivo db.sqlite3

Inicialze novamente a API:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

Abra o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador para verificar se a aplicacao esta no ar.


