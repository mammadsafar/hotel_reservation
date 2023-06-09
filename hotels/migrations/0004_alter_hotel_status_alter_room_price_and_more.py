# Generated by Django 4.1 on 2023-05-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_remove_hotel_state_remove_hotel_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='status',
            field=models.CharField(choices=[('yes', 'فعال'), ('no', 'غیرفعال')], max_length=3, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6, verbose_name='قیمت (تومان)'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_Type',
            field=models.CharField(choices=[('1', 'یک تخته'), ('2', 'دو تخته'), ('3', 'سه تخته'), ('4', 'چهارتخته'), ('5', 'پنج تخته')], max_length=1, verbose_name='نوع اتاق'),
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('yes', 'فعال'), ('no', 'غیرفعال')], max_length=3, verbose_name='وضعیت'),
        ),
    ]
