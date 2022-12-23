from django.contrib import admin
from .models import Post

# Register your models here.


class PostFilter(admin.ModelAdmin):
    list_filter = [
        "title",
        "description",
    ]
    search_fields = (
        "title",
        "description",
    )


admin.site.register(Post, PostFilter)
