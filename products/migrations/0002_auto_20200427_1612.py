# Generated by Django 3.0.5 on 2020-04-27 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Book',
        ),
        migrations.RemoveField(
            model_name='category',
            name='books',
        ),
    ]
