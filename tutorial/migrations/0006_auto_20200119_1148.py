# Generated by Django 3.0.2 on 2020-01-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_auto_20200119_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='const',
            name='const',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
