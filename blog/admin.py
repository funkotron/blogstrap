from django.contrib import admin
from blog.models import Post, Tag, Social


class TaggedInline(admin.TabularInline):
    model = Post.tags.through
    #extra = 3

class TagAdmin(admin.ModelAdmin):
    inlines= [
        TaggedInline,
    ]

    
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields':['name','slug','body']}),
        ('Settings',        {'fields':['datetime','page'], 'classes':['collapse']}),

    ]
    inlines = [TaggedInline]
    exclude = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Social)