# Generated by Django 3.2 on 2021-05-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210507_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='popup_media',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='popup_source_link',
            field=models.CharField(default='test', max_length=120),
            preserve_default=False,
        ),
    ]
