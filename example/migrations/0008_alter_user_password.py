# Generated by Django 4.1.3 on 2023-12-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]