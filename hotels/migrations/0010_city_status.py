# Generated by Django 4.2.2 on 2023-06-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_alter_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='status',
            field=models.CharField(choices=[('yes', 'فعال'), ('no', 'غیرفعال')], default=1, max_length=3, verbose_name='وضعیت'),
            preserve_default=False,
        ),
    ]
