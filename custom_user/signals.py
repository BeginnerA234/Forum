from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from backend import settings
from custom_user.models import Country
from custom_user.validators.username_validator import custom_username_validator

User = settings.AUTH_USER_MODEL



@receiver(signal=pre_save, sender=User)
def validate_username_field(sender, instance, *args, **kwargs):
    """
    Валидируем username перед сохранением в базу
    """
    custom_username_validator(instance.username)

@receiver(pre_delete, sender=Country)
def delete_picture(sender, instance, **kwargs):
    if instance.picture:
        instance.picture.delete(False)
