<h1 align="center">Users API Python</h1>

### :clipboard: Funcionalidade
<p>
  Projeto realizado em Python capaz de realizar as operações básicas de um CRUD de Usuário (Criar, Listar todos os usuários, Listar usuário, Deletar usuário e Atualizar usuário). Nesse projeto, foi utilizado o MongoDb Atlas como meio para salvar e buscar os dados.
</p>

### :computer: Pré-requisitos para execução
- [x] IDE para execução de códigos Python (ex: Visual Studio Code)
- [x] [Python 3](https://www.python.org/downloads/)
- [x] Bibliotecas Utilizadas: Flask, PyMongo, Flask-PyMongo
### :rocket: Começando
<p>Para obter uma cópia do projeto a fim de operá-lo na sua máquina, clone o repositório em uma pasta na sua máquina:</p>

```
$ git clone git@github.com:RafaelaPapale/usersPython-api.git
```
### :wrench: Instalação e Execução

**Instalação:**
<p>Caso nenhuma das bibliotecas utilizadas no projeto esteja previamente instalada no seu computador, insira os seguintes comandos em seu terminal (garanta que o gerenciador de pacotes do Python (pip) esteja instalado em seu computador):</p>
```
$ pip install pymongo

$ pip install flask

$ pip install Flask-PyMongo
```

**Execução:**
<p>Após clonar, garanta que o terminal esteja no diretório da pasta principal do projeto.</p>

```
$ cd usersPython-api
```

<p>Então, insira o seguinte comando:</p>

```
$ export FLASK_APP=main.py
```

<p>Depois execute o comando a seguir para subir o backEnd:</p>

```
$ python3 -m flask run
```
### :telescope: Rotas

- POST[/user]: Realiza a criação de um usuário passando os parâmetros *name, amount_products e company*.
- PUT[/user/:id]: Realiza a atualização dos dados de um usuário passando os parâmetros *name, amount_products e company* no body da requisição e o id no path.
- GET[/user]: Realiza a busca de todos os usuários cadastrados.
- GET[/user/:id]: Realiza a busca do usuário cujo id foi passado no path da requisição.
- DELETE[/user/:id]: Realiza a remoção do usuário cujo id foi passado no path da requisição.

### :hammer: Construído com...

**IDE**: [Visual Studio Code](https://code.visualstudio.com/)

**Tecnolgias**: [Python 3](https://www.python.org/downloads/)

**Pertinência**: [MongoDb Atlas](https://account.mongodb.com/account/login?_ga=2.204523984.1347496482.1648473728-1771549431.1644318985&_gac=1.90835432.1648487392.CjwKCAjwuYWSBhByEiwAKd_n_ku0vCvysMHVuTLai3cSowiu8WJUE7xhE8tnfrgID6XgQz8zTzOemRoCY8AQAvD_BwE)

**Controle de versões**: [GitHub](https://github.com/)