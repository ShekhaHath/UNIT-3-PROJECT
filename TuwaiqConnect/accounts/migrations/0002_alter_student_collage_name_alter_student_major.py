# Generated by Django 5.0.2 on 2024-04-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='collage_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=255),
        ),
    ]