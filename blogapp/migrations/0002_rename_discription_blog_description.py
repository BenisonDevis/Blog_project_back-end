# Generated by Django 5.0.7 on 2024-07-17 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='discription',
            new_name='description',
        ),
    ]
