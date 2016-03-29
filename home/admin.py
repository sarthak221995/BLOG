from django.contrib import admin
from .models import Post,Tag




class TagAdmin(admin.ModelAdmin):
    list_display = ('title_tag',)

    class Meta:
    	model=Tag

    
		




class PostAdmin(admin.ModelAdmin):
	list_filter = ['created','modified']
	list_display = ('title','author','modified','featured','draft',)
	list_editable = ["featured",'draft',]
	search_fields = ["title","author",'tag_field',]


	class Meta:
		model=Post

admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
