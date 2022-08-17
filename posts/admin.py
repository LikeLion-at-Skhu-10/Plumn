from django.contrib import admin
from .models import Post, Feedback, Objection #Photo, 


#admin.site.register(Post, PostAdmin)

# photo 클래스를 inline으로 나타낸다.
#class Photo(admin.TabularInline):
#    models = Photo

#Post 클래스는 해당하는 photo 객체를 관리한다.
#class PostAdmin(admin.ModelAdmin):
#    inlines = [PhotoInline, ]

admin.site.register(Feedback)
admin.site.register(Objection)
admin.site.register(Post)