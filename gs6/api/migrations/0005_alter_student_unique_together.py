# Generated by Django 4.0.6 on 2022-08-16 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_student_unique_together_alter_student_roll'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('id', 'roll')},
        ),
    ]
