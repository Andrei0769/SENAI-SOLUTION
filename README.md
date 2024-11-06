SENAI Solution
Este é um projeto de sistema de gerenciamento de usuários desenvolvido como parte do curso técnico do SENAI. Ele permite o cadastro, pesquisa, atualização e exclusão de usuários, além de exibir todos os usuários cadastrados, com persistência dos dados em um banco de dados MySQL.

Funcionalidades
No arquivo principal do sistema, há um menu de navegação para selecionar a ação desejada. O menu é exibido até que o usuário opte por sair. As opções incluem:

Adicionar usuário
Pesquisar um usuário
Atualizar dados de um usuário
Excluir um usuário
Exibir todos os usuários cadastrados
Sair
Ao escolher uma opção, o sistema realiza a operação correspondente no banco de dados e retorna a mensagem apropriada para o usuário.

Tecnologias Utilizadas
Python: linguagem de programação principal do projeto
Testes Automatizados: Pytest
ORM: SQLAlchemy para mapeamento objeto-relacional e manipulação do banco de dados
Banco de Dados: MySQL
Containerização: Docker para empacotamento da aplicação
Orquestração de Contêineres: Docker Compose para configuração e gerenciamento de múltiplos contêineres
Versionamento: Git para controle de versões e branches do projeto
Estrutura do Código
O código é estruturado para que os dados sejam salvos no banco de dados MySQL utilizando o SQLAlchemy como ORM, e todas as operações do CRUD estão implementadas em funções específicas.

Observações
Testes: Os testes automatizados verificam a integridade dos dados e garantem que as operações de CRUD funcionem conforme o esperado. A biblioteca Pytest é usada para a execução desses testes.
Tratamento de Exceções: Todos os erros e exceções são tratados e exibidos ao usuário sem interromper a execução do programa.
Versionamento: O desenvolvimento é organizado por meio de branches no Git, permitindo melhor gerenciamento e controle de versões do código.