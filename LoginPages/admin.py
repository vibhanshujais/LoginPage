from django.contrib import admin
from LoginPages.models import signupdata

class SignUpDatas(admin.ModelAdmin):
    data = ('full_name', 'username', 'contact', 'email_id', 'password')


admin.site.register(signupdata, SignUpDatas)
