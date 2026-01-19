# 🍽️ **Sabor IFS (Aplicação de Restaurante) – Manual Completo para Usuário, Administrador e Desenvolvedor**

**Versão:** 1.5.0
**Framework:** Django 5.2
**Público:** Usuários, Administradores, Desenvolvedores
**Autores:** Adriny Safira, Cauan Ugino, Cleiton Matheus, Cristiano Brito, Elton Moraes

---

# 📚 **Índice Geral**

1. [Introdução](#1-introdução)

2. [Estrutura da Aplicação](#2-estrutura-da-aplicação)

3. [Guia do Usuário](#3-guia-do-usuário)
   - Home
   - Menu
   - Carrinho
   - Checkout
   - Pedidos
   - Perfil
   - Feedback
   - Reserva de Mesas

4. [Guia de Logística ](#4-guia-de-logística)
   - Lista de Entregas
   - Detalhes da Entrega
   - Atualização de Status
   - Atribuição de Entregadores
   - Cadastro de Entregadores

5. [Guia do Administrador](#5-guia-do-administrador)

6. [Guia do Desenvolvedor](#6-guia-do-desenvolvedor)
   - Instalação
   - Estrutura do Projeto
   - Modelos
   - Rotas
   - APIs
   - Testes
   - Debug
   - Deploy

7. [Imagens](#7-imagens)

8. [Conclusão](#8-conclusão)

---

# **1. Introdução**

O **Restaurant Web Application** é um sistema moderno e completo para restaurantes com:

🍔 Cardápio dinâmico <br>
🛒 Carrinho inteligente <br>
💳 Finalização de pedidos <br>
📦 Rastreamento de entregas <br>
🚴‍♂️ Sistema de entregadores <br>
📱 Painel do cliente <br>
🛠 Painel administrativo <br>
📅 Reserva de mesas <br>
Envio de feedback <br>

O sistema foi expandido para incluir **gestão logística completa**, permitindo:

- cadastro de entregadores
- controle de entregas
- atualização de status
- atribuição manual de entregadores
- detalhes completos das entregas
- notas e rastreamento

---

# **2. Estrutura da Aplicação**

A aplicação possui **três níveis de acesso**:

---

## 🔓 **Páginas Públicas**

Qualquer usuário pode acessar:

- Home
- Menu
- Sobre
- Feedback
- Reservas
- Contato
- Login / Cadastro

---

## 🔐 **Páginas do Usuário Autenticado**

Usuário logado pode acessar:

- Carrinho
- Checkout
- Meus Pedidos
- Perfil
- Logout

---

## 🛠 **Páginas Administrativas**

Requer:

```python
user.is_staff = True
```

Inclui:

- Dashboard
- Pedidos
- Itens do cardápio
- Feedback
- Reservas
- Gestão logística
- Entregadores
- Entregas e status

---

# **3. GUIA DO USUÁRIO**

Aprenda a navegar pelo site.

---

## 📍 **3.1 – Home**

Contém:

- Banner principal
- Destaques do restaurante
- Pratos populares
- Depoimentos
- Botões de ação rápida

![Home Page 1](images/inicio-1.png)
![Home Page 2](images/inicio-2.png)
![Home Page 3](images/inicio-3.png)
![Home Page 4](images/inicio-4.png)

---

## 📍 **3.2 – Entrar**

Formulário para acessar a aplicação
![Entrar](images/login.png)

---

## 📍 **3.3 – Cadastrar**

Formulário para fazer cadastro para ter acesso a aplicação

## ![Cadastrar](images/register.png)

## 📍 **3.4 – Menu**

A página exibe:

- Foto
- Título
- Descrição
- Preço
- Botão “Adicionar ao Carrinho”

![navigation_menu](images/menu-3.png)

Como usar:

1. Role pela lista de pratos
2. Clique em **Adicionar ao Carrinho**
3. Recebe feedback visual de confirmação

---

## 🛒 **3.5 – Carrinho**

Elementos na página:

- lista de itens
- quantidades
- preço total
- botões para remover
- botões para aumentar/diminuir

![cart_page](images/cart.png)

Funções:

- ➕ aumentar quantidade
- ➖ diminuir quantidade
- ❌ remover item
- ✔ seguir para o checkout

---

## 💳 **3.6 – Checkout**

Exibe:

- resumo do pedido
- total final
- itens e quantidades
- botão “Finalizar Pedido”

![checkout_page](images/checkout.png)

Ao finalizar:

- cria `Order`
- cria `OrderItem`
- limpa carrinho
- redireciona para o resumo

---

## 📦 **3.7 – Resumo do Pedido**

Mostra:

- ID
- data
- itens
- total
- status

![order_summary](images/order_summary.png)

---

## 📑 **3.8 – Meus Pedidos**

Histórico completo.

![my_orders_page](images/my_orders_page.png)

---

## 👤 **3.9 – Perfil do Usuário**

Inclui:

- nome
- email
- data do cadastro
- total de pedidos

![profile_page](images/profile.png)

---

## **3.10 – Feedback**

Formulário com:

- nome
- nota
- mensagem
- foto opcional

![feedback_form](images/feedback_form.png)

---

## 🍽 **3.11 – Reservas**

Formulário simples:

![table_booking](images/table_booking.png)

---

# **4. GUIA DE LOGÍSTICA**

Grande novidade do sistema.

---

## 🚚 **4.1 – Lista de Entregas**

URL:
`/dashboard/deliveries/`
![Lista de Entregas](images/meus-pedidos-lista.png)
Exibe:

- número do pedido
- status atual
- entregador responsável
- botão "Detalhes"

Funções:

- visualizar todas as entregas
- acessar cada pedido individual

---

## 📄 **4.2 – Detalhes da Entrega**

URL:
`/dashboard/delivery/<id>/`
![Detalhes da Entrega](images/ger-entrega.png)
Exibe:

- dados do pedido
- status
- histórico
- notas
- entregador atual

Permite ações:

- alterar status
- adicionar notas
- atribuir entregador

---

## 🔄 **4.3 – Atualizar Status da Entrega**

URL POST:
`/dashboard/delivery/<id>/update/`
![Atualizar status da entrega](images/atualizar-status-pedido.png)
Status disponíveis:

- pendente
- em rota
- entregue
- cancelado

A página contém:

- dropdown de status
- textarea para notas
- botão salvar

---

## 🧍‍♂️ **4.4 – Atribuir Entregador**

URL POST:

`/dashboard/delivery/<id>/assign/`
![Atualizar status do entregador](images/atualizar-status-pedido.png)
Selecione:

- nenhum entregador
- algum entregador cadastrado

Define o responsável pela entrega.

---

## 👷‍♂️ **4.5 – Cadastro de Entregadores**

URL:
`/dashboard/delivery-person/`
![Entregadores](images/entregadores.png)
URL para adicionar:
`/dashboard/delivery-person/add/`
![Addicionar entregador](images/add-entregador.png)

Campos:

- nome
- telefone

---

# **5. GUIA DO ADMINISTRADOR**

Painel administrativo completo.
![Admin](images/admin.png)

---

# **6. GUIA DO DESENVOLVEDOR**

## 🛠 **6.1 – Instalação**

```bash
git clone https://github.com/eltonmoraes6/restaurant-django-app.git
cd restaurant-django-app
```

Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie o usuário administrador:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

App: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

---

## 🧱 **6.2 – Estrutura do Projeto**

```
restaurant-django-app/
│
├── Base_App/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── cms/
│   │   ├── categories/
│   │   ├── delivery/
│   │   └── admin/
│   ├── static/
│
├── Resturant_Project/
│   ├── settings.py
│   ├── urls.py
│
├── media/
├── static/
├── init_cms.py
├── requirements.txt
└── README.md
```

---

## 🧩 **6.3 – Modelos**

### Principais:

- Category – categorias do cardápio
- Items – produtos
- Cart – carrinho temporário
- Order – pedido
- OrderItem – itens do pedido
- BookTable – reserva de mesa
- Feedback – avaliações
- Delivery – logística da entrega
- DeliveryPerson – entregadores
- CMSContent / PageSection – conteúdo dinâmico do site

---

## 🧭 **6.4 – Rotas**

### Carrinho

| URL               |       View        |
| :---------------- | :---------------: |
| `/add-to-cart/`   |    add_to_cart    |
| `/cart/`          |   CartPageView    |
| `/increase/<id>/` | increase_quantity |
| `/decrease/<id>/` | decrease_quantity |

### 🚚 Logística / Entregas

| URL                                |          View          |
| :--------------------------------- | :--------------------: |
| `/dashboard/deliveries/`           |     delivery_list      |
| `/dashboard/delivery/<id>/`        |    delivery_detail     |
| `/dashboard/delivery/<id>/update/` |    delivery_update     |
| `/dashboard/delivery/<id>/assign/` |    delivery_assign     |
| `/dashboard/delivery-person/`      |  delivery_person_list  |
| `/dashboard/delivery-person/add/`  | delivery_person_create |

### 🧩 CMS (Gerenciamento de Conteúdo)

| URL               |       View       |
| :---------------- | :--------------: |
| `/cms/`           | Lista de seções  |
| `/cms/create/`    | Criar nova seção |
| `/cms/edit/<id>/` | Editar conteúdo  |

---

## 📝 **6.5 – CMS (Como Funciona)**

O CMS permite **editar textos, títulos e imagens do site sem alterar código**.

### 📌 Páginas suportadas:

- Home
- About
- Menu
- Footer
- Contact

Cada página pode conter **múltiplas seções**, como:

- Hero
- Texto institucional
- Rodapé
- Informações de contato

---

### ➕ Criar Conteúdo Manualmente (Painel)

1. Acesse: `/cms/`
2. Clique em **Adicionar Nova Seção**
3. Escolha:
   - Página (home, about, footer…)
   - Seção (ex: hero, description, footer_about)

4. Preencha título, conteúdo e imagem
5. Salve

O conteúdo passa a aparecer automaticamente no site.

---

## ⚙️ **6.6 – Inicialização Automática do CMS (Seed)**

Para criar conteúdo inicial automaticamente, use o script **init_cms.py**.

### Exemplo de conteúdo padrão:

```python
defaults = [
    ("about", "title", "We Are Feane"),
    ("about", "description", "We began our journey in 1990..."),
]
```

### Executar o seed:

```bash
python manage.py shell < init_cms.py
```

✔ Ideal para ambientes novos
✔ Evita banco vazio
✔ Facilita deploy e testes

---

## 🌐 **6.7 – API (Exemplo)**

Resposta ao adicionar item no carrinho:

```json
{
  "message": "Item adicionado com sucesso",
  "quantity": 1
}
```

---

## 🧪 **6.8 – Testes**

```bash
python manage.py test
```

---

## 🐞 **6.9 – Debug Comum**

| Erro                 | Solução                |
| -------------------- | ---------------------- |
| NoReverseMatch       | Verificar nome da rota |
| TemplateDoesNotExist | Caminho do template    |
| ImportError          | Caminho incorreto      |
| 404                  | URL não registrada     |

---

## 🚀 **6.10 – Deploy (Produção)**

```bash
pip install gunicorn whitenoise
```

Adicione:

```python
"whitenoise.middleware.WhiteNoiseMiddleware",
```

Execute:

```bash
gunicorn Resturant_Project.wsgi
```

# **7. IMAGENS**

![alt text](images/inicio-1.png)
![alt text](images/inicio-2.png)
![alt text](images/inicio-3.png)
![alt text](images/inicio-4.png)

![navigation_menu](images/menu.png)

![alt text](images/login.png)
![alt text](images/register.png)

![navigation_menu](images/menu-2.png)
![navigation_menu](images/menu-3.png)

![alt text](images/cart-popup.png)
![alt text](images/cart.png)
![alt text](images/checkout.png)
![alt text](images/order_summary.png)
![alt text](images/my_orders_page.png)
![alt text](images/meus-pedidos-lista.png)

![alt text](images/nosso-cardapio.png)
![alt text](images/sobre.png)
![alt text](images/reservar-mesa.png)
![alt text](images/table_booking.png)
![alt text](images/feedback.png)
![alt text](images/feedback_form.png)

![alt text](images/menu-3.png)
![alt text](images/profile.png)
![alt text](images/my_orders_page.png)

![alt text](images/admin_dashboard.png)
![alt text](images/admin_dashboard-02.png)

![alt text](images/cms.png)
![alt text](images/produtos-lista.png)
![alt text](images/add-produto.png)
![alt text](images/add-categoria.png)
![alt text](images/ger-pedidos.png)
![alt text](images/ger-entrega.png)
![alt text](images/entregadores.png)
![alt text](images/add-entregador.png)

![alt text](images/admin.png)

# **8. CONCLUSÃO**

O Sabor IFS foi desenvolvido com o objetivo de oferecer uma solução completa e integrada para a gestão de restaurantes, unindo praticidade, organização e eficiência em um único sistema. Ao longo deste manual, foram apresentados os principais recursos da aplicação, contemplando as necessidades de usuários, administradores e desenvolvedores, de forma clara e estruturada.

Para o usuário final, a aplicação disponibiliza funcionalidades essenciais como visualização do cardápio, gerenciamento do carrinho, finalização de pedidos, acompanhamento do histórico, envio de feedbacks e realização de reservas de mesas, proporcionando uma experiência intuitiva e acessível. Já para o administrador, o sistema oferece um painel robusto para controle de produtos, categorias, pedidos, avaliações, reservas e logística, incluindo o gerenciamento de entregas e entregadores, garantindo maior organização e controle operacional.

Do ponto de vista técnico, o projeto foi construído utilizando o framework Django 5.2, seguindo boas práticas de desenvolvimento, com uma arquitetura modular, controle de acesso por níveis de permissão e integração de um CMS, que permite a atualização dinâmica de conteúdos sem a necessidade de alterações diretas no código. O guia do desenvolvedor fornece orientações completas para instalação, manutenção, testes e deploy, facilitando a continuidade e evolução do sistema.

Dessa forma, o Sabor IFS apresenta-se como uma aplicação estável, escalável e preparada para uso em ambientes reais, além de servir como uma base sólida para futuras melhorias e expansões. Este manual tem como finalidade apoiar o uso correto da plataforma e contribuir para a sua manutenção e desenvolvimento contínuo.
