# Generated by Django 4.1.6 on 2023-02-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('anons', models.CharField(max_length=200)),
                ('full_text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'name',
                'verbose_name_plural': 'names',
            },
        ),
    ]
