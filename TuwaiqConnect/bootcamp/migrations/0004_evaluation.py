# Generated by Django 5.0.2 on 2024-04-11 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_student_gpa'),
        ('bootcamp', '0003_delete_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_rate', models.FloatField()),
                ('grades_rate', models.FloatField()),
                ('bootcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bootcamp.bootcamp')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
    ]
