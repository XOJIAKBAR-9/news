# Generated by Django 5.1.3 on 2024-12-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_gallery_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default=1, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
