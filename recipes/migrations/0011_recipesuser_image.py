# Generated by Django 5.1.2 on 2024-11-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesuser',
            name='image',
            field=models.ImageField(blank=True, default='/images/default_photo.jpg', null=True, upload_to='images'),
        ),
    ]