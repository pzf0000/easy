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
                if hasattr(new_class, item):
                    model_admin_attr_dict[item] = getattr(new_class, item)

        class_name = str(new_class.__name__) + "Admin"
        ModelAdminClass = type(class_name, (admin.ModelAdmin,), model_admin_attr_dict)

        admin.site.register(new_class, ModelAdminClass)
        admin.site.site_header = "Easy MicroService for Database"
        admin.site.site_title = "Easy Django MicroService for Database"
        return new_class


class AdminModel(models.Model, metaclass=AdminModelBase):
    """
    Some attributes in admin.ModelAdmin, it can be prompted automatically when writing code in the IDE
    """
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []

