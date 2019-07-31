from django.contrib import admin

from blog import models


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Post, PostAdmin)
