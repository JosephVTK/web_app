from django.contrib import admin


# Register your models here.

MODEL_EXAMPLE = """

from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)

"""
