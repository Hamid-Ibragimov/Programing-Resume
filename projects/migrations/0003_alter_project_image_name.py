# Generated by Django 3.2 on 2021-05-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
