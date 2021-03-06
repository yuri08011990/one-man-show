# Generated by Django 3.0.8 on 2020-07-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва курсу')),
                ('description', models.TextField(verbose_name='Опис курсу')),
                ('start', models.CharField(max_length=100, verbose_name='Дата початку курсу')),
                ('end', models.CharField(max_length=100, verbose_name='Дата закінчення курсу')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]
