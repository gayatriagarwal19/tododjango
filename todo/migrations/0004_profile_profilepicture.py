# Generated by Django 4.0.4 on 2022-08-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_profile_alter_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ProfilePicture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
