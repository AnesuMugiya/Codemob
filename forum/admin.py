from django.contrib import admin
from .models import Post, Answer, Comment, UpVote, DownVote, Flame

class PostAdmin(admin.ModelAdmin):
     list_display=('title', 'created_by')
     search_fields=('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(UpVote)
admin.site.register(DownVote)