# Album Meetups

O **Album Meetups** é uma aplicação web desenvolvida com Django que permite aos usuários organizar e compartilhar álbuns musicais associados a encontros e eventos.  
Com uma interface intuitiva, os usuários podem cadastrar álbuns, associá-los a eventos específicos e visualizar detalhes relevantes.

## Funcionalidades

- Cadastro e gerenciamento de álbuns musicais
- Associação de álbuns a eventos (meetups)
- Upload de capas de álbuns e imagens relacionadas
- Visualização de detalhes dos álbuns e eventos

## Funcionalidades

- Criação e gerenciamento de eventos (meetups)
- Upload e organização de imagens em álbuns
- Visualização de eventos e fotos associadas
- Interface amigável para facilitar a navegação e interação

## Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/) - Framework web em Python
- HTML, CSS - Para estrutura e estilização das páginas
- [Gunicorn](https://gunicorn.org/) - Servidor WSGI para aplicações Python
- [Heroku](https://www.heroku.com/) - Plataforma para deploy da aplicação

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```md
album_meetups/
├── django_site/ # Configurações do projeto Django
├── meetups/ # Aplicativo principal com modelos e views
├── uploads/ # Diretório para armazenar imagens enviadas
├── manage.py # Script de gerenciamento do Django
├── requirements.txt # Dependências do projeto
└── Procfile # Arquivo para deploy no Heroku**
```

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/rmendes1/album_meetups.git
   cd album_meetups
   ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Instale as dependências:**
 
    ```bash
    pip install -r requirements.txt
    ```

5. **Aplique as migrações:**

    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

6. **Acesse a aplicação:**

Abra o navegador e vá para `http://localhost:8000/`.
