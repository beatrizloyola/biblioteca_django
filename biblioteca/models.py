from django.db import models

import datetime
from django.utils import timezone


class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    autor = models.TextField(null=False)
    anoPublicacao = models.IntegerField(null=False)
    isbn = models.TextField(null=False)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.titulo

    def string_detalhada(self):
        return "id: " + str(self.id) + "; titulo: " + "; autor: " + self.autor + "; ano publicação: " + str(self.anoPublicacao) + "; isbn: " + str(self.isbn)
