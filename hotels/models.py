from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class City(models.Model):
    STATES_CHOICES = (
        ('TE', 'تهران'),
        ('RK', 'خراسان رضوی'),
        ('FA', 'فارس'),
        ('HR', 'هرمزگان'),
        ('IS', 'اصفهان'),
        ('QO', 'قم'),
        ('AL', 'البرز'),
        ('AR', 'اردبیل'),
        ('EA', 'آدربایجان غربی'),
        ('WE', 'آذربایجان شرقی'),
        ('BU', 'بوشهر'),
        ('CH', 'چهارمحال و بختیاری'),
        ('GI', 'گیلان'),
        ('GO', 'گلستان'),
        ('HA', 'همدان'),
        ('IL', 'ایلام'),
        ('KE', 'کرمان'),
        ('KZ', 'کرمانشاه'),
        ('KH', 'خوزستان'),
        ('KB', 'کهگلویه و بویراحمد'),
        ('KR', 'کردستان'),
        ('LO', 'لرستان'),
        ('MK', 'مرکزی'),
        ('MA', 'مازندران'),
        ('NK', 'خراسان شمالی'),
        ('QA', 'قزوین'),
        ('SB', 'سیستان و بلوچستان'),
        ('SK', 'خراسان جنوبی'),
        ('SM', 'سمنان'),
        ('YA', 'یزد'),
        ('ZA', 'رنجان')
    )
    STATUS_CHOICES = (
        ('yes', 'فعال'),
        ('no', 'غیرفعال'),
    )
    status = models.CharField(verbose_name='وضعیت', choices=STATUS_CHOICES, max_length=3)
    state = models.CharField(verbose_name='استان', choices=STATES_CHOICES, max_length=2)
    city = models.CharField(verbose_name='شهر', max_length=200)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return f"{self.get_state_display()} - {self.city}"


class Hotel(models.Model):
    STATUS_CHOICES = (
        ('yes', 'فعال'),
        ('no', 'غیرفعال'),
    )
    name = models.CharField(verbose_name='نام هتل', max_length=200)
    description = RichTextUploadingField(verbose_name='توضیحات', )
    class_hotel = models.IntegerField(verbose_name='کلاس هتل (چند ستاره)',
                                      validators=[MaxValueValidator(5), MinValueValidator(1)])
    city = models.ForeignKey(City, verbose_name='شهر', related_name='hotel', on_delete=models.CASCADE)
    address = models.CharField(verbose_name='آدرس', max_length=600)
    status = models.CharField(verbose_name='وضعیت', choices=STATUS_CHOICES, max_length=3)
    cover = models.ImageField(verbose_name='تصویر شاخص', upload_to='hotels/covers/', blank=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel_detail', args=[self.id])  # /book/1


class Gallery(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='هتل', related_name='galley', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='تصویر', upload_to='hotels/gallery', blank=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)


class Room(models.Model):
    ROOM_TYPE_CHOICES = (
        ('1', 'یک تخته'),
        ('2', 'دو تخته'),
        ('3', 'سه تخته'),
        ('4', 'چهارتخته'),
        ('5', 'پنج تخته'),
    )
    STATUS_CHOICES = (
        ('yes', 'فعال'),
        ('no', 'غیرفعال'),
    )
    hotel = models.ForeignKey(Hotel, verbose_name='هتل', related_name='room', on_delete=models.CASCADE)
    room_Type = models.CharField(verbose_name='نوع اتاق', choices=ROOM_TYPE_CHOICES, max_length=1)
    capacity = models.IntegerField(verbose_name='ظرفیت', validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                   default=0)
    price = models.DecimalField(verbose_name='قیمت (تومان)', max_digits=8, decimal_places=0)
    status = models.CharField(verbose_name='وضعیت', choices=STATUS_CHOICES, max_length=3)

    breakfast = models.BooleanField(verbose_name='صبحانه', default=True)
    extra_bed = models.BooleanField(verbose_name='تخت اضافه', default=False)

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)


class Discount(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='هتل', related_name='discount', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='اتاق', related_name='discount', on_delete=models.CASCADE)

    discount = models.IntegerField(verbose_name='تخفیف (درصد)',
                                   validators=[MaxValueValidator(100), MinValueValidator(0)],
                                   default=0)

    start_date = models.DateTimeField(verbose_name='تاریخ شروع')
    end_date = models.DateTimeField(verbose_name='تاریخ پایان')

    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)
