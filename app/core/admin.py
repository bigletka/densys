"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

admin.site.register(models.User)
admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Appointment)
