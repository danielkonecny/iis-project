# Generated by Django 2.2.6 on 2019-10-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(default='Sport', max_length=50, unique=True),
        ),
    ]
