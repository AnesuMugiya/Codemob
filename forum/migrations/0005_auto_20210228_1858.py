# Generated by Django 3.1.5 on 2021-02-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210226_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
