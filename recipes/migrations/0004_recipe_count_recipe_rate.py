# Generated by Django 5.0.6 on 2024-09-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_creator_alter_recipesuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]