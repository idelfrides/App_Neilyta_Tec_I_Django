# Generated by Django 2.2.1 on 2019-05-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursodjango', '0009_auto_20190530_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professores',
            name='anoInicio',
            field=models.CharField(max_length=4),
        ),
    ]