# Generated by Django 4.0.6 on 2022-07-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_title',
            field=models.CharField(max_length=20),
        ),
    ]
