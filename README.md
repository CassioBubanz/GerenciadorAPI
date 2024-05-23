Gerenciador de Usuários e Itens
Este projeto é uma API desenvolvida em Django que oferece funcionalidades para o gerenciamento de usuários e itens. Ele fornece endpoints RESTful para criar, atualizar, excluir e recuperar informações de usuários e itens. Este sistema é ideal para aplicações que necessitam de um backend robusto para a gestão de usuários e inventário.

Funcionalidades:
Gerenciamento de Usuários
 - Criação de novos usuários com nome de usuário e senha exclusivos
 - Autenticação de usuários
 - Atualização de informações de perfil de usuários (nome completo, e-mail, etc.)
 - Recuperação de informações de perfil de usuários
 
Gerenciamento de Itens
 - Criação de novos itens com nome e preço
 - Atualização do nome e preço dos itens
 - Exclusão de itens
 - Recuperação de uma lista de todos os itens

Tecnologias Utilizadas
 - Django
 - Django REST Framework
 - SQLite (ou outro banco de dados compatível com Django)
 - Python 3.12.3

Como Rodar o Projeto
1. Clone o repositório:
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Crie e ative um ambiente virtual:
   python -m venv myenv
   source myenv/bin/activate  # No Windows: myenv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Aplique as migrações do banco de dados:
   python manage.py makemigrations
   python manage.py migrate

5. Inicie o servidor:
   python manage.py runserver
