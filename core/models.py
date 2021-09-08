from django.db import models
from django.utils.translation import gettext_lazy as _


# TimeStamp Mixin:
class TimeStamp(models.Model):
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created time"),
        help_text=_("This is created time")
    )
    modify_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Modified time"),
        help_text=_("This is modified time")
    )

    class Meta:
        abstract = True


# BaseManager :
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # define method for access all querysets
    def get_archive(self):
        return super().get_queryset()

    # define method for access all active query
    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define deactive item
    def get_deactive_list(self):
        return self.get_queryset().filter(is_active=False)


# Logical Model :
class LogicalModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Deleted status"),
        help_text=_("This is deleted status")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        help_text=_("This is active status")
    )

    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.is_deleted = True
        self.save()

    def deactive(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
