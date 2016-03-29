from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_filter = ['created']
	list_display = ('created','name','email_id')

admin.site.register(Post,PostAdmin)
