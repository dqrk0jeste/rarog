# Generated by Django 4.1.3 on 2024-03-14 21:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.user')),
            ],
        ),
    ]
