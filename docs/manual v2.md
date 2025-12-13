# 🍽️ **Restaurant Web Application – Manual Completo para Usuário, Administrador e Desenvolvedor**

**Versão:** 1.5.0
**Framework:** Django 5.2
**Público:** Usuários, Administradores, Desenvolvedores
**Autor:** Elton Moraes

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

4. [Guia de Logística (NOVO)](#4-guia-de-logística-novo)

   - Lista de Entregas
   - Detalhes da Entrega
   - Atualização de Status
   - Atribuição de Entregadores
   - Cadastro de Entregadores

5. [Guia do Administrador](#5-guia-do-administrador)

6. [Guia do Desenvolvedor (COMPLETO)](#6-guia-do-desenvolvedor-completo)

   - Instalação
   - Estrutura do Projeto
   - Modelos
   - Rotas
   - APIs
   - Testes
   - Debug
   - Deploy

7. [Imagens](#7-dicas-para-adicionar-imagens)

8. [Conclusão](#8-conclusão)

---

# ⭐ **1. Introdução**

O **Restaurant Web Application** é um sistema moderno e completo para restaurantes com:

🍔 Cardápio dinâmico
🛒 Carrinho inteligente
💳 Finalização de pedidos
📦 Rastreamento de entregas (NOVO)
🚴‍♂️ Sistema de entregadores (NOVO)
📱 Painel do cliente
🛠 Painel administrativo
📅 Reserva de mesas
⭐ Envio de feedback

O sistema foi expandido para incluir **gestão logística completa**, permitindo:

- cadastro de entregadores
- controle de entregas
- atualização de status
- atribuição manual de entregadores
- detalhes completos das entregas
- notas e rastreamento

---

# ⭐ **2. Estrutura da Aplicação**

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
- Gestão logística (NOVO)
- Entregadores (NOVO)
- Entregas e status (NOVO)

---

# ⭐ **3. GUIA DO USUÁRIO**

Aqui o usuário aprende a navegar pelo site.

---

## 📍 **3.1 – Home**

Contém:

- Banner principal
- Destaques do restaurante
- Pratos populares
- Depoimentos
- Botões de ação rápida

![Menu Page](images/menu.png)

---

## 📍 **3.2 – Menu**

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

## 🛒 **3.3 – Carrinho**

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

## 💳 **3.4 – Checkout**

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

## 📦 **3.5 – Resumo do Pedido**

Mostra:

- ID
- data
- itens
- total
- status

![order_summary](images/order_summary.png)

---

## 📑 **3.6 – Meus Pedidos**

Histórico completo.

![my_orders_page](images/my_orders_page.png)

---

## 👤 **3.7 – Perfil do Usuário**

Inclui:

- nome
- email
- data do cadastro
- total de pedidos

![profile_page](images/profile.png)

---

## ⭐ **3.8 – Feedback**

Formulário com:

- nome
- nota
- mensagem
- foto opcional

![feedback_form](images/feedback_form.png)

---

## 🍽 **3.9 – Reservas**

Formulário simples:

![table_booking](images/table_booking.png)

---

# ⭐ **4. GUIA DE LOGÍSTICA (NOVO)**

Grande novidade do sistema.

---

## 🚚 **4.1 – Lista de Entregas**

URL:
`/dashboard/deliveries/`

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

Selecione:

- nenhum entregador
- algum entregador cadastrado

Define o responsável pela entrega.

---

## 👷‍♂️ **4.5 – Cadastro de Entregadores**

URL:
`/dashboard/delivery-person/`

URL para adicionar:
`/dashboard/delivery-person/add/`

Campos:

- nome
- telefone

---

# ⭐ **5. GUIA DO ADMINISTRADOR**

Painel administrativo completo.

---

# ⭐ **6. DEVELOPER GUIDE (COMPLETO)**

Aqui entra **a seção integral que você pediu**, INALTERADA, traduzida e formatada.

---

## 🛠 **6.1 – Instalação**

```bash
git clone https://github.com/eltonmoraes6/restaurant-django-app.git
cd restaurant-django-app
```

Crie o ambiente:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

Instale dependências:

```bash
pip install -r requirements.txt
```

Migre:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie admin:

```bash
python manage.py createsuperuser
```

Executar server:

```bash
python manage.py runserver
```

---

## 🧱 **6.2 – Estrutura do Projeto**

```
restaurant-django-app/
│
├── Base_App/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   ├── static/
│   ├── forms.py
│
├── Resturant_Project/
│   ├── settings.py
│   ├── urls.py
│
├── media/
├── static/
├── requirements.txt
└── README.md
```

---

## 🧩 **6.3 – Modelos**

### Principais:

- Items
- Cart
- Order
- OrderItem
- BookTable
- Feedback
- Delivery (NOVO)
- DeliveryPerson (NOVO)

---

## 🧭 **6.4 – Rotas**

### Carrinho

| URL | View |
| `/add-to-cart/` | add_to_cart |
| `/cart/` | CartPageView |
| `/increase/<id>/` | increase_quantity |
| `/decrease/<id>/` | decrease_quantity |

### Logística

| URL | view |
| `/dashboard/deliveries/` | delivery_list |
| `/dashboard/delivery/<id>/` | delivery_detail |
| `/dashboard/delivery/<id>/update/` | delivery_update |
| `/dashboard/delivery/<id>/assign/` | delivery_assign |
| `/dashboard/delivery-person/` | delivery_person_list |
| `/dashboard/delivery-person/add/` | delivery_person_create |

---

## 🌐 **6.5 – API**

Exemplo:

```json
{
  "message": "Item adicionado com sucesso",
  "quantity": 1
}
```

---

## 🧪 **6.6 – Testes**

```bash
python manage.py test
```

---

## 🐞 **6.7 – Debug**

| Erro                 | Solução                |
| -------------------- | ---------------------- |
| NoReverseMatch       | Verificar nome da rota |
| TemplateDoesNotExist | Caminho do template    |
| ImportError          | Caminho incorreto      |

---

## 🚀 **6.8 – Deploy**

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

---

# ⭐ **7. Dicas para adicionar imagens**

---

# ⭐ **8. Conclusão**

Este manual documenta **todo o sistema**, incluindo:

✔ funcionalidades novas
✔ logística
✔ entregadores
✔ atribuição
✔ atualizações de status
✔ usabilidade
✔ desenvolvimento

---
