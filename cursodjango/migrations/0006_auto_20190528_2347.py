# Generated by Django 2.2.1 on 2019-05-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursodjango', '0005_auto_20190528_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professores',
            old_name='curso',
            new_name='cursoLec',
        ),
        migrations.AddField(
            model_name='professores',
            name='formacao',
            field=models.CharField(default='Eng. Computação', max_length=100),
        ),
    ]