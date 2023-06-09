# Generated by Django 4.2.2 on 2023-06-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='/media/avatars/default.png', null=True, upload_to='avatars/'),
        ),
    ]
