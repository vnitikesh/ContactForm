# Generated by Django 2.1.7 on 2020-09-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
