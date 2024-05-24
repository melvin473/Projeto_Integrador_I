# Importando os módulos necessários
from django.forms import ModelForm
from django import forms
from .models import Animal, Evento

# Atribuição de valores para os widgets do formulário
castrado_item = ("Sim","Sim"),("Não","Não")
sexo_item = ("Macho","Macho"), ("Fêmea","Fêmea")
status_item = ('Perdido',"Perdido"), ('Encontrado',"Encontrado"), ('Para adoção',"Para adoção")

# Criando a classe AnimalForm
class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nome_pet', 'raca_pet', 'idade_pet', 'sexo_pet', 'castrado_pet', 'endereco_pet', 'contato_pet', 'status_pet', 'detalhes_pet', 'imagem_pet', 'data_hora_pet']
        widgets = {
            'nome_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'raca_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'idade_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'sexo_pet' : forms.RadioSelect(choices=sexo_item, attrs={"class":"form-check-input"}),
            'castrado_pet' : forms.RadioSelect(choices=castrado_item, attrs={"class":"form-check-input"}),
            'endereco_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'contato_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block", "placeholder":"*Telefone ou WhatsApp*"}),
            'status_pet' : forms.RadioSelect(choices=status_item, attrs={"class":"form-check-input"}),
            'detalhes_pet' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block", "rows":"4", "placeholder": "*** Escreva mais detalhes sobre o que aconteceu ***"}),
            'imagem_pet' : forms.FileInput(attrs={"class":"form-control-file"}),
            'data_hora_pet' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"})
            }

# Criando a classe Evento        
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nome_evento', 'tipo_evento', 'data_evento', 'local_evento', 'detalhes_evento', 'imagem_evento']
        widgets = {
            'nome_evento' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'tipo_evento' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'data_evento' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'local_evento' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'detalhes_evento' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block", "rows":"4", "placeholder": "*** Escreva mais detalhes sobre o evento ***"}),
            'imagem_evento' : forms.FileInput(attrs={"class":"form-control-file"})
            }