# Generated by Django 5.0.6 on 2024-09-22 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like_count',
        ),
    ]
