# Generated by Django 4.2.2 on 2023-06-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='nome',
            field=models.TextField(default='sem nome', max_length=255),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='imagens/projetos'),
        ),
    ]
