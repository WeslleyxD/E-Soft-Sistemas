# Generated by Django 4.0.3 on 2022-03-29 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testepratico', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuarios',
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['nome', 'sobrenome']},
        ),
    ]
