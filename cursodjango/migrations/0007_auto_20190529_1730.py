# Generated by Django 2.2.1 on 2019-05-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursodjango', '0006_auto_20190528_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name_plural': 'Evento'},
        ),
        migrations.AlterField(
            model_name='evento',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]