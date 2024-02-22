from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'status',
    ]
    fieldsets = (
        (None, {
            "fields": (
                'title' ,'body'
            ),
        }),
        ('important dates' , {
            'fields':('create_date' ,'modify_date')
        }),
        ('status',{
            'fields':('status',)
        })
    )
    
    readonly_fields=('create_date' ,'modify_date')
    
    list_filter = ('status' ,)
    search_fields=('title','author__username')