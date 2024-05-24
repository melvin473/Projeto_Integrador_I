# Generated by Django 5.0.4 on 2024-05-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0010_alter_animal_data_hora_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=20)),
                ('nome_evento', models.CharField(max_length=20, verbose_name='Nome do evento:')),
                ('tipo_evento', models.CharField(max_length=20, verbose_name='Tipo de evento:')),
                ('data_evento', models.CharField(max_length=20, verbose_name='Data')),
                ('detalhes_pet', models.CharField(max_length=280, verbose_name='Detalhes:')),
                ('imagem_pet', models.ImageField(upload_to='media', verbose_name='Foto:')),
            ],
        ),
    ]