# Generated by Django 3.2.8 on 2021-11-23 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moradias', '0003_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Imagem',
        ),
        migrations.RenameField(
            model_name='imagem',
            old_name='docfile',
            new_name='arquivo',
        ),
    ]
