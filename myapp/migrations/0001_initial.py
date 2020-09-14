# Generated by Django 2.1.7 on 2020-09-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=55)),
                ('contact', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]