# encoding: utf-8

from django.contrib import admin

# Classe Post do CMS
from .models import Post

# Registra no modulo de administracao
admin.site.register(Post)

