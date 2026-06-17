# Sistema de Aluguel de Carros

## Descrição

O Sistema de Aluguel de Carros é uma aplicação web desenvolvida em Python utilizando o framework Django. O objetivo do sistema é gerenciar o processo de locação de veículos, permitindo o cadastro de carros, clientes, funcionários e contratos de aluguel, além do acompanhamento de devoluções e emissão de contratos em PDF.

O sistema possui controle de acesso por autenticação de usuários e oferece uma interface administrativa para gerenciamento das informações.

---

## Funcionalidades

### Veículos

* Cadastro de veículos.
* Edição e remoção de veículos.
* Controle de quantidade disponível.
* Cadastro de imagem do veículo.
* Definição do valor da diária.

### Clientes

* Cadastro automático durante a locação.
* Consulta de clientes cadastrados.
* Histórico de locações por cliente.

### Aluguéis

* Registro de locação de veículos.
* Controle de quantidade de dias.
* Cálculo automático do valor da locação.
* Registro da forma de pagamento.
* Controle de devolução.
* Histórico de locações.

### Funcionários

* Cadastro de funcionários.
* Controle de acesso ao sistema.
* Login individual por usuário.

### Contratos

* Geração automática de contrato em PDF.
* Impressão do contrato para assinatura do cliente.

### Dashboard

* Quantidade total de veículos.
* Quantidade de veículos alugados.
* Quantidade de veículos disponíveis.
* Total de clientes cadastrados.
* Receita total do sistema.
* Próximas devoluções.
* Últimos aluguéis realizados.

---

## Tecnologias Utilizadas

### Linguagem de Programação

* Python 3.x

### Framework

* Django 5.x

### Banco de Dados

* SQLite 3

### Front-end

* HTML5
* CSS3
* Bootstrap Icons

### Geração de PDF

* ReportLab

### Controle de Versão

* Git
* GitHub

---

## Requisitos

Antes de executar o sistema, certifique-se de possuir instalado:

* Python 3.10 ou superior
* Pip
* Git

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/Sistema-de-aluguel-de-carros.git
```

### 2. Acessar a pasta do projeto

```bash
cd Sistema-de-aluguel-de-carros
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Aplicar migrações

```bash
python manage.py migrate
```

### 7. Criar administrador

```bash
python manage.py createsuperuser
```

Informe:

* Nome de usuário
* E-mail
* Senha

### 8. Executar servidor

```bash
python manage.py runserver
```

---

## Acesso ao Sistema

Após iniciar o servidor, acessar:

```text
http://127.0.0.1:8000/
```

Painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

Utilize o usuário e senha criados pelo comando:

```bash
python manage.py createsuperuser
```

---

## Estrutura do Sistema

### Administrador

Possui acesso total ao sistema:

* Cadastro de veículos.
* Cadastro de funcionários.
* Administração completa do sistema.

### Funcionário

Possui acesso operacional:

* Realização de aluguéis.
* Consulta de clientes.
* Consulta de contratos.
* Registro de devoluções.

---

## Autor

Eduardo Alves

Projeto desenvolvido para fins de estudo e aplicação prática dos conceitos de desenvolvimento web com Django.
