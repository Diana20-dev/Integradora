# Generated by Django 3.0.6 on 2020-08-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200810_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='curriculum',
            field=models.FileField(null=True, upload_to='curriculums'),
        ),
    ]
