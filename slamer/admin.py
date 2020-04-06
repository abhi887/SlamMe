from django.contrib import admin
from slamer.models import *

admin.site.site_header="SlamMe"
admin.site.site_title="SlamMe"

admin.site.register(user)
admin.site.register(abs_user)
admin.site.register(slam_request)
admin.site.register(slam_post)
