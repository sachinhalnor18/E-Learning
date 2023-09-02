from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Videos,Contact

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)

class cc(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Contact, cc)

