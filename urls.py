from django.urls import path
from .views import home, termos, cadastropet, animais, mural, cadastroevento

urlpatterns = [
    path('', home),
    path('home', home),
    path('termos', termos),
    path('cadastropet', cadastropet),
    path('animais', animais),
    path('mural', mural),
    path('cadastroevento', cadastroevento)
]