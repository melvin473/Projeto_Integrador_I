# Importando os módulos necessários
from django.shortcuts import render
from .models import Animal, Evento
from .forms import AnimalForm, EventoForm
from django.http import HttpResponseRedirect

# Página inicial
def home(request):
    return render(request, "home.html")

# Termos de Uso
def termos(request):
    return render(request, "termos.html")

# Cadastro de animais
def cadastropet(request):
    # Se a requisição for do tipo POST, validar o formulário e gravar no banco de dados
    if request.method == "POST":
        # Cria uma nova instância do formulário e preenche com os dados da requisição
        form = AnimalForm(request.POST, request.FILES)
        # Checando se o formulário é válido:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("animais") # Redireciona para a página de animais
    
    # Se a requisição for do tipo GET retornar um formulário em branco
    else:
        form = AnimalForm()
        return render(request, "cadastropet.html", {"form": form})

# Exibe os animais cadastrados    
def animais(request):
    obj = Animal.objects.all()
    contexto = {'obj': obj}
    return render(request, "animais.html", contexto)

# Mural de eventos
def cadastroevento(request):
    # Se a requisição for do tipo POST, validar o formulário e gravar no banco de dados
    if request.method == "POST":
        # Cria uma nova instância do formulário e preenche com os dados da requisição
        form = EventoForm(request.POST, request.FILES)
        # Checando se o formulário é válido:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("mural") # Redireciona para a página de eventos
    
    # Se a requisição for do tipo GET retornar um formulário em branco
    else:
        form = EventoForm()
        return render(request, "cadastroevento.html", {"form": form})
    
def mural(request):
    obj = Evento.objects.all()
    contexto = {'obj': obj}
    return render(request, "mural.html", contexto)