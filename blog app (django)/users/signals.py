from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import profileModel    
from django.dispatch import receiver


# @receiver(post_save, sender = User)
# def create_profile(sender, instance,created,*args, **kwargs):
#     if created:
#         profileModel.objects.create(user=instance)

