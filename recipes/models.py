from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=65, verbose_name=_("Nome"))
    # slug = models.SlugField(unique=True, max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "category"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        

class Recipe(models.Model):
    title = models.CharField(max_length=65, verbose_name=_("Título"))
    description = models.CharField(max_length=165, verbose_name=_("Descrição"))
    preparation_time = models.IntegerField(verbose_name=_("Tempo de Preparo"))
    # preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField(verbose_name=_("Quantidade de Porção"))
    # servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField(verbose_name=_("Texto"))
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', verbose_name=_("Imagem"))
    category = models.OneToOneField(
        Category, on_delete=models.SET_NULL, null=True, verbose_name=_("Categoria")
    )
    author = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = "recipe"
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
                


    

