from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 65)

class Recipe(models.Model):
    title = models.CharField(max_length = 65)
    description = models.CharField(max_length = 165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length = 10)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length = 10)
    preparation_steps = models.TextField()  
    preparation_steps_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to = 'recipes/covers/%Y/%m/%d/')
    # category recebe a chave estrangeira da tabela Category e é setado como nulo para que possa ser criado um registro sem que seja necessário informar a categoria
    category = models.ForeignKey(
        Category, on_delete = models.SET_NULL, null = True
    )
    # author recebe a chave estrangeira da tabela User e é setado como nulo para que possa ser criado um registro sem que seja necessário informar o autor
    author = models.ForeignKey(
        User, on_delete = models.SET_NULL, null = True
    )

    # se caso tivessemos um models.CASCADE, ao deletar um usuário, todos os registros de receitas associados a ele seriam deletados

    # se caso tivessemos um models.PROTECT, ao deletar um usuário, não seria possível deletar um usuário que tenha receitas associadas a ele

    # se caso tivessemos um models.SET_NULL, ao deletar um usuário, os registros de receitas associados a ele teriam o campo author setado como nulo

    # se caso tivessemos um models.SET_DEFAULT, ao deletar um usuário, os registros de receitas associados a ele teriam o campo author setado com um valor padrão

    # se caso tivessemos um models.SET, ao deletar um usuário, os registros de receitas associados a ele teriam o campo author setado com um valor específico
    
    # se caso tivessemos um models.DO_NOTHING, ao deletar um usuário, os registros de receitas associados a ele não seriam afetados
    

# Create your models here.
