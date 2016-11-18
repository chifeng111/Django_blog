from django.contrib import admin
from blog.models import Blog
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['标题','更新时间']
    list_display_links = ['更新时间']
    list_editable = ['标题']
    search_fields = ['标题','内容']
    class Meta:
        model = Blog

admin.site.register(Blog, BlogModelAdmin)