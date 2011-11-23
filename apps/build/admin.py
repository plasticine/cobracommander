from django.contrib import admin

from .models.build import Build
from .models.step import Step
from .models.target import Target

admin.site.register(Build)
admin.site.register(Step)
admin.site.register(Target)
