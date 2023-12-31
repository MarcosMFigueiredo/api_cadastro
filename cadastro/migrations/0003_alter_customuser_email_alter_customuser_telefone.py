# Generated by Django 4.2.5 on 2023-09-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_rename_full_name_customuser_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]
