# Generated by Django 4.0.3 on 2022-03-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('sobrenome', models.CharField(max_length=40)),
                ('idade', models.CharField(max_length=2)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]