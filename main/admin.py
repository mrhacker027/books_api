from django.contrib import admin
import main.models as models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    ...
    
# Register your models here.
