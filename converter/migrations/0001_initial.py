# Generated by Django 4.2 on 2023-04-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SvgFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Название')),
                ('link', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Ссылка')),
                ('type', models.CharField(db_index=True, max_length=7, verbose_name='Тип')),
            ],
        ),
    ]
