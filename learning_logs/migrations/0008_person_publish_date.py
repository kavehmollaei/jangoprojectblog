# Generated by Django 3.2.2 on 2021-05-07 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_topic_upload_image_for_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
