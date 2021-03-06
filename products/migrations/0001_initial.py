# Generated by Django 3.0.5 on 2020-04-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('books', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=50)),
                ('published_date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('page_count', models.IntegerField()),
                ('thumbnail_url', models.CharField(max_length=300)),
                ('language', models.CharField(max_length=10)),
                ('authors', models.CharField(max_length=300)),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]
