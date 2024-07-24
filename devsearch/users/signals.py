from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

        # UDEMY LECTURE 30: I need to set up 2fa for email account to allow less secure access to use
        # the below functionality
        
        # subject = 'Welcome to DevSearch'
        # message = f'Hi {profile.username}, we are glad to have you join us! Welcome to our platform'

        # send_mail(
        #     subject=subject,
        #     message=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[profile.email],
        #     fail_silently=False
        # )



def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)