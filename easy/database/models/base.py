from django.db import models
from django.db.models.base import ModelBase
from django.contrib import admin

from nameko.rpc import rpc
from nameko.containers import ServiceContainer


class AdminModelBase(ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        new_class = super().__new__(cls, name, bases, attrs, **kwargs)
        model_admin_dir = dir(admin.ModelAdmin)

        model_admin_attr_dict = {}
        for item in model_admin_dir:
            if not item.startswith('_'):
                if item in kwargs:
                    model_admin_attr_dict[item] = cls.__getattribute__(item)

        class_name = str(new_class.__name__) + "Admin"
        ModelAdminClass = type(class_name, (admin.ModelAdmin,), model_admin_attr_dict)

        admin.site.register(new_class, ModelAdminClass)
        admin.site.site_header = "Easy MicroService for Database"
        admin.site.site_title = "Easy Django MicroService for Database"
        return new_class


class AdminModel(models.Model, metaclass=AdminModelBase):
    pass

