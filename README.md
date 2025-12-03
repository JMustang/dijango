# Django Training Project 🐍

Projeto de treinamento em Python Django para aprender os fundamentos do framework web mais popular do Python.

## 📋 Sobre o Projeto

Este é um projeto educacional criado para praticar e aprender Django. Atualmente contém:

- Configuração básica do Django 5.2.8
- App `todos` criado (pronto para implementação)
- Views simples de exemplo
- Banco de dados SQLite configurado

## 🚀 Como Começar

### Pré-requisitos

- Python 3.14 ou superior
- [uv](https://github.com/astral-sh/uv) instalado (gerenciador de pacotes)

### Instalação

1. Clone o repositório (ou navegue até a pasta do projeto)
2. Instale as dependências:

```bash
uv sync
```

3. Execute as migrações (quando criar modelos):

```bash
uv run --directory tutorialProject python manage.py migrate
```

4. Crie um superusuário (opcional):

```bash
uv run --directory tutorialProject python manage.py createsuperuser
```

5. Inicie o servidor de desenvolvimento:

```bash
uv run --directory tutorialProject python manage.py runserver
```

6. Acesse no navegador:

- <http://127.0.0.1:8000/> - Página inicial
- <http://127.0.0.1:8000/hello> - View de exemplo
- <http://127.0.0.1:8000/admin/> - Painel administrativo

## 📁 Estrutura do Projeto

```
dijango/
├── tutorialProject/          # Projeto Django principal
│   ├── core/                 # Configurações do projeto
│   │   ├── settings.py       # Configurações
│   │   ├── urls.py           # URLs principais
│   │   └── ...
│   ├── todos/                # App de tarefas (a implementar)
│   │   ├── models.py         # Modelos de dados
│   │   ├── views.py          # Views/Controladores
│   │   ├── urls.py           # URLs do app
│   │   └── ...
│   ├── manage.py             # Script de gerenciamento
│   └── db.sqlite3            # Banco de dados SQLite
├── pyproject.toml            # Dependências do projeto
└── README.md                 # Este arquivo
```

## 🎯 Próximos Passos - Backend

### 1. Criar Modelos de Dados (Models)

**Implementar o modelo Todo:**

```python
# tutorialProject/todos/models.py
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

**Comandos:**

```bash
uv run --directory tutorialProject python manage.py makemigrations
uv run --directory tutorialProject python manage.py migrate
```

### 2. Registrar no Admin

**Adicionar ao admin.py:**

```python
# tutorialProject/todos/admin.py
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at']
    list_filter = ['completed', 'created_at']
    search_fields = ['title', 'description']
```

### 3. Criar Views com Templates

**Opções de implementação:**

- **Function-Based Views (FBV)** - Mais simples, ideal para iniciantes
- **Class-Based Views (CBV)** - Mais reutilizáveis, padrão Django moderno
- **Django REST Framework** - Para criar APIs REST

**Exemplo de view com template:**

```python
# tutorialProject/todos/views.py
from django.shortcuts import render, get_object_or_404
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/list.html', {'todos': todos})
```

### 4. Criar Templates HTML

**Estrutura de templates:**

```
tutorialProject/
└── todos/
    └── templates/
        └── todos/
            ├── base.html      # Template base
            ├── list.html      # Lista de todos
            ├── detail.html    # Detalhes de um todo
            └── form.html      # Formulário
```

### 5. Implementar CRUD Completo

- **Create** - Criar novas tarefas
- **Read** - Listar e visualizar tarefas
- **Update** - Editar tarefas existentes
- **Delete** - Remover tarefas

### 6. Adicionar Formulários Django

```python
# tutorialProject/todos/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
```

### 7. Implementar Autenticação de Usuários

- Sistema de login/logout
- Registro de novos usuários
- Proteção de rotas com `@login_required`
- Relacionar todos com usuários (`ForeignKey`)

### 8. Adicionar Validações e Testes

- Validações de formulário
- Testes unitários com `unittest` ou `pytest`
- Testes de integração

### 9. Adicionar API REST (Opcional)

**Instalar Django REST Framework:**

```bash
uv add djangorestframework
```

**Criar serializers e viewsets:**

```python
# tutorialProject/todos/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
```

## 🎨 Próximos Passos - Frontend

### 1. Melhorar Templates com CSS

**Opções:**

- **CSS puro** - Criar arquivos CSS customizados
- **Bootstrap** - Framework CSS popular
- **Tailwind CSS** - Framework utility-first
- **Bulma** - Framework CSS moderno

**Estrutura de arquivos estáticos:**

```
tutorialProject/
└── todos/
    └── static/
        └── todos/
            ├── css/
            │   └── style.css
            ├── js/
            │   └── main.js
            └── images/
```

### 2. Adicionar JavaScript Interativo

**Funcionalidades sugeridas:**

- Validação de formulários no frontend
- Confirmação de exclusão com JavaScript
- Filtros e busca em tempo real
- Drag and drop para reordenar tarefas
- Marcar como concluído sem recarregar página (AJAX)

### 3. Implementar Design Responsivo

- Mobile-first approach
- Media queries para diferentes tamanhos de tela
- Menu hambúrguer para mobile

### 4. Adicionar Animações e Transições

- Transições suaves entre páginas
- Animações ao adicionar/remover itens
- Loading states e spinners

### 5. Criar SPA (Single Page Application) - Opcional

**Opções:**

- **HTMX** - Adiciona interatividade sem JavaScript complexo
- **Alpine.js** - Framework JavaScript minimalista
- **React/Vue** - Frameworks modernos (com API REST)

### 6. Melhorar UX/UI

- Mensagens de feedback (sucesso/erro)
- Paginação para listas grandes
- Filtros e ordenação
- Dark mode
- Ícones (Font Awesome, Heroicons, etc.)

## 🔧 Melhorias Técnicas

### Backend

- [ ] Adicionar logging
- [ ] Configurar variáveis de ambiente (python-decouple)
- [ ] Adicionar cache (Redis/Memcached)
- [ ] Implementar paginação
- [ ] Adicionar filtros avançados (django-filter)
- [ ] Configurar CORS (se criar API)
- [ ] Adicionar rate limiting
- [ ] Implementar busca full-text
- [ ] Adicionar signals do Django
- [ ] Criar comandos customizados (management commands)

### Frontend

- [ ] Otimizar imagens
- [ ] Minificar CSS/JS
- [ ] Implementar service workers (PWA)
- [ ] Adicionar acessibilidade (ARIA)
- [ ] SEO básico (meta tags)
- [ ] Implementar lazy loading

## 📚 Recursos de Aprendizado

- [Documentação Oficial do Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Real Python - Django](https://realpython.com/tutorials/django/)

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+**
- **Django 5.2.8**
- **SQLite** (banco de dados)
- **uv** (gerenciador de pacotes)

## 📝 Notas

- Este é um projeto de aprendizado
- O banco de dados SQLite é adequado para desenvolvimento
- Para produção, considere PostgreSQL ou MySQL
- Sempre use migrações para alterar modelos

## 🤝 Contribuindo

Este é um projeto pessoal de treinamento, mas sinta-se livre para experimentar e adicionar novas funcionalidades!
