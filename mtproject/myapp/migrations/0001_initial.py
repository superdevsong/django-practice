# Generated by Django 4.0.6 on 2022-07-20 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=200)),
                ('board_text', models.TextField()),
            ],
        ),
    ]
