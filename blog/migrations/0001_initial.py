# Generated by Django 5.1.2 on 2024-11-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('sign_of_publication', models.BooleanField(default=False, verbose_name='признак публикации')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
        ),
    ]