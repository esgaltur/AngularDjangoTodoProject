from django.contrib import admin


from rest_api.models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ['description', 'targetDate','IsDone','user']

admin.site.register(Todo, TodoAdmin)
