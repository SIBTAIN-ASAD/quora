# Generated by Django 5.0 on 2024-01-07 02:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_vote_answer_alter_vote_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
