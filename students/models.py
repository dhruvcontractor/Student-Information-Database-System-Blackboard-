from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib import messages


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    banner_id = models.TextField(max_length=9)
    address = models.TextField(max_length=200)
    phone = models.TextField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    total_credit = models.TextField(max_length=9)
    balance = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class Profile(models.Model):
    STUDENT = 1
    FACULTY = 2
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1, blank=True)
    banner_id = models.TextField(max_length=9)
    gpa = models.DecimalField(max_digits=3, default=0.00, decimal_places=2)
    total_credit = models.TextField(max_length=9)
    balance = models.DecimalField(max_digits=7, default=0.00, decimal_places=2)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
    def get_absolute_url(self):
        url = reverse("students:detail", args=[str(self.id)])
        return url

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
