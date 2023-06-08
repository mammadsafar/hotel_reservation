from django.contrib import admin
from .models import City, Hotel, Gallery, Room, Discount


@admin.register(City)
class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('state', 'city', 'created_at')
    list_filter = ('state', 'city', 'created_at')
    search_fields = ('state', 'city')
    ordering = ('city',)


@admin.register(Hotel)
class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('name', 'city', 'class_hotel', 'status', 'created_at')
    list_filter = ('city', 'class_hotel', 'created_at')
    search_fields = ('name', 'state', 'city')
    ordering = ('-created_at', 'class_hotel')


@admin.register(Room)
class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('hotel', 'room_Type', 'price', 'breakfast', 'extra_bed', 'status', 'created_at')
    list_filter = ('hotel', 'room_Type', 'price', 'breakfast', 'extra_bed', 'status', 'created_at')
    search_fields = ('hotel', 'room_Type')
    ordering = ('-created_at', 'discount',)


@admin.register(Discount)
class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('room', 'discount', 'start_date', 'end_date', 'created_at')
    list_filter = ('room', 'discount', 'start_date', 'end_date', 'created_at')
    search_fields = ('room', 'start_date', 'end_date')
    ordering = ('-created_at',)


admin.site.register(Gallery)
# admin.site.register(Comment, CommentAdmin)
