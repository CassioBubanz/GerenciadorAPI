GerenciadorAPI
Este projeto é um sistema de gerenciamento de usuários, itens e pedidos, construído com Django e Django Rest Framework.

Funcionalidades

Gerenciamento de Usuários
 - Criação de novos usuários com nome de usuário, e-mail e senha.
 - Atualização de informações do usuário, incluindo nome, e-mail e senha.
 - Exclusão de usuários do sistema.
 - Recuperação de uma lista de todos os usuários cadastrados.

Gerenciamento de Itens
 - Criação de novos itens com nome e preço.
 - Atualização do nome e preço de um item existente.
 - Exclusão de itens do sistema.
 - Recuperação de uma lista de todos os itens cadastrados.

Gerenciamento de Pedidos
 - Criação de novos pedidos para um usuário, contendo um ou vários itens.
 - Recuperação de todos os pedidos de um usuário.
 - Recuperação de detalhes de um pedido específico, incluindo os itens associados.

Estrutura do Projeto
O projeto está estruturado da seguinte forma:

 - users: Contém os modelos, serializers e viewsets relacionados aos usuários.
 - itens: Contém os modelos, serializers e viewsets relacionados aos itens.
 - pedidos: Contém os modelos, serializers e viewsets relacionados aos pedidos.
 - api: Contém as views e rotas da API.

Configuração e Uso
 1. Clone o repositório: git clone https://github.com/CassioBubanz/GerenciadorAPI.git
 2. Instale as dependências: pip install -r requirements.txt
 3. Execute as migrações do banco de dados: python manage.py migrate
 4. Inicie o servidor: python manage.py runserver
 5. Acesse a API em http://localhost:8000/
