# Generated by Django 3.2.5 on 2021-07-17 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NotesApp', '0003_notes_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='index',
        ),
    ]
