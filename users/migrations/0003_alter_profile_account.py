# Generated by Django 3.2.9 on 2021-12-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211223_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.CharField(choices=[('Guest', 'Guest'), ('Mentor', 'Mentor'), ('Mentee', 'Mentee')], default='Guest', max_length=6),
        ),
    ]