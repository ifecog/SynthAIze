# Generated by Django 5.1.1 on 2024-09-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
