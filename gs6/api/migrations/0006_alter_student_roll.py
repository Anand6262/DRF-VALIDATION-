# Generated by Django 4.0.6 on 2022-08-16 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_student_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
    ]
