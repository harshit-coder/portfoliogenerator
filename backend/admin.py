from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
# Register your models here.
from backend.models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from django.contrib.auth.models import User

from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)



class education_admin(admin.TabularInline):
    model = education


class key_specialization_admin(admin.TabularInline):
    model = key_specialization


class certification_admin(admin.TabularInline):
    model = certification


class key_achievements_admin(admin.TabularInline):
    model = key_achievements


class skill_admin(admin.TabularInline):
    model = skill


class trait_admin(admin.TabularInline):
    model = trait


class projects_admin(admin.TabularInline):
    model = projects


class social_url_admin(admin.TabularInline):
    model = social_url


class internships_admin(admin.TabularInline):
    model = internships


class jobs_admin(admin.TabularInline):
    model = jobs


class introadmin(admin.ModelAdmin):
    inlines = [education_admin,social_url_admin,key_specialization_admin,certification_admin,key_achievements_admin,skill_admin,trait_admin,projects_admin,internships_admin,jobs_admin]

    class Meta:
        model = Intro


admin.site.register(Intro, introadmin)

