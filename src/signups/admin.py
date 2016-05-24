from django.contrib import admin

# Register your models here.

from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)