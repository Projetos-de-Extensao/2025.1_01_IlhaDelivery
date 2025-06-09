---
id: diagrama_de_caso_de_uso
title: Diagrama de Caso de Uso
---


# Diagrama de Caso de Uso 1.0

Este documento descreve as funcionalidades do sistema Ilha Delivery da perspectiva dos usuários, conhecidos como "atores". Ele ilustra as diferentes maneiras pelas quais os atores podem interagir com a aplicação para atingir seus objetivos.

---

### 1. Atores

Identificamos dois atores principais no sistema:

* **Cliete (Usuário)**: O usuário principal da aplicação. É qualquer pessoa que se cadastra no sistema para solicitar entregas de produtos.
* **Administrador**: Um usuário com privilégios elevados, geralmente um membro da equipe do Ilha Delivery. Ele possui todas as permissões de um Cliente e, adicionalmente, pode gerenciar os dados do sistema.
* **Sistema**: O sistema que conttrola a conexão do cliente e do administrador

---

### 2. Casos de Uso

A seguir estão os principais casos de uso (funcionalidades) disponíveis para cada ator.

#### Casos de Uso do Cliente

* **Autenticar-se**: Permite que o cliente acesse o sistema de forma segura usando suas credenciais.
* **Gerenciar Perfil Pessoal**: O cliente pode visualizar e atualizar suas informações de cadastro, como nome, endereço e contato.
* **Criar Pedido**: O cliente pode fazer um novo pedido, especificando os produtos, observações e forma de pagamento.
* **Consultar Histórico de Pedidos**: O cliente pode visualizar todos os pedidos que já realizou.
* **Acompanhar Status do Pedido**: Permite ao cliente verificar o andamento de um pedido em aberto (ex: "Em Preparo", "A Caminho").

#### Casos de Uso do Administrador

O Administrador pode realizar todas as ações de um Cliente e também:

* **Visualizar Todos os Pedidos**: Tem acesso à lista completa de pedidos de todos os clientes.
* **Gerenciar Entregadores**: Pode cadastrar, visualizar e atualizar as informações dos entregadores.
* **Gerenciar Clientes**: Tem acesso à lista de todos os clientes cadastrados no sistema.

---

### 3. Diagrama
![![Diagrama de Caso de Uso](../assets/diagrama_caso_de_uso/Diagrama%20de%20caso%20de%20uso.png)](../assets/diagrama_caso_de_uso/Diagrama%20de%20caso%20de%20uso.png)




# Diagrama de Caso de Uso 2.0

---

### 1. Atores

* **Cliente**: O usuário final da plataforma. É responsável por se cadastrar, gerenciar sua conta e realizar/acompanhar pedidos.
* **Entregador**: O profissional responsável pela logística de entrega. Ele utiliza o sistema para visualizar suas tarefas e atualizar o progresso da entrega.
* **Administrador**: O usuário com permissões de gerenciamento sobre toda a plataforma. É responsável por administrar os dados de clientes, entregadores e pedidos.

---

### 2. Casos de Uso

A seguir, estão as funcionalidades (casos de uso) disponíveis para cada ator, de acordo com o diagrama.

#### Casos de Uso do Cliente

* **Cadastrar-se**: Permite que um novo usuário crie uma conta de cliente.
* **Gerenciar Conta**: Permite ao cliente, após logado, atualizar suas informações pessoais.
* **Realizar Pedido**: Funcionalidade central para o cliente fazer uma nova solicitação de entrega.
* **Acompanhar Status do Pedido**: Permite ao cliente verificar o andamento de um pedido.
* **Ver Histórico de Pedidos**: O cliente pode visualizar todos os pedidos que já realizou.

#### Casos de Uso do Entregador

* **Ver Pedidos Atribuídos**: Permite ao entregador visualizar a lista de entregas que deve realizar.

#### Casos de Uso do Administrador

* **Gerenciar Pedidos**: Permite visualizar, editar e atribuir todos os pedidos do sistema.
* **Gerenciar Clientes**: Permite visualizar e administrar os dados dos clientes cadastrados.
* **Gerenciar Entregadores**: Permite cadastrar, editar e remover entregadores da plataforma.

---

### 3. Diagrama 


![![Diagrama de Caso de Uso](../assets/diagrama_caso_de_uso/Diagrama%20de%20caso%20de%20uso%202.png)](../assets/diagrama_caso_de_uso/Diagrama%20de%20caso%20de%20uso%202.png)

