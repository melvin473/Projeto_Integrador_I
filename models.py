# Importando os módulos necessários
from django.db import models

# Criando a classe Animal para registrar os pets perdidos
class Animal(models.Model):
    id_usuario = models.CharField(max_length=20)
    nome_pet = models.CharField(max_length=20, verbose_name="Nome:")
    raca_pet = models.CharField(max_length=20, verbose_name="Raça:")
    idade_pet = models.CharField(max_length=20, verbose_name="Idade:")
    sexo_pet = models.CharField(max_length=5, verbose_name="Sexo:")
    castrado_pet = models.CharField(max_length=3, verbose_name="Castrado:")
    endereco_pet = models.CharField(max_length=50, verbose_name="Endereço:")
    contato_pet = models.CharField(max_length=20, verbose_name="Contato:")
    status_pet = models.CharField(max_length=11, verbose_name="Situação:")
    detalhes_pet = models.CharField(max_length=280, verbose_name="Detalhes:")
    imagem_pet = models.ImageField(upload_to="media", verbose_name="Foto do animal:")
    data_hora_pet = models.CharField(max_length=50, verbose_name="Data da ocorrência:")
    
    def __str__(self):
        return self.nome_pet
    
class Evento(models.Model):
    id_usuario = models.CharField(max_length=20)
    nome_evento = models.CharField(max_length=20, verbose_name="Nome do evento:")
    tipo_evento = models.CharField(max_length=20, verbose_name="Tipo de evento:")
    data_evento = models.CharField(max_length=20, verbose_name="Data:")
    local_evento = models.CharField(max_length=20, verbose_name="Local:")
    detalhes_evento = models.CharField(max_length=280, verbose_name="Detalhes:")
    imagem_evento = models.ImageField(upload_to="media", verbose_name="Foto:")
    
    def __str__(self):
        return self.nome_evento