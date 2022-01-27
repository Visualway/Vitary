from django.db import models
from django.contrib.auth.models import User
from apps.vit.models import Vit

from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()

class Abuse(models.Model):
    """
    Abuse model
    """
    ABUSE_TYPE = (
        ('1', 'Abuse'),
        ('2', 'Inappropriate'),
        ('3', 'Spam'),
        ('4', 'Bullying'),
        ('5', 'Sexual Content'),
        ('6', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    abuse_type = models.CharField(max_length=50, choices=ABUSE_TYPE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    to_vit = models.ForeignKey(Vit, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Abuses'
        ordering = ['-date']
        

class Badge(models.Model):
    """
    Badge model
    """

    COLOR_CHOICE = (
        ('success', 'Green'),
        ('info', 'Blue'),
        ('link', 'Purple'),
        ('primary', 'Turquoise'),
        ('warning', 'Yellow'),
        ('danger', 'Red'),
        ('dark', 'Black'),
        ('white', 'White'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICE)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Requirments(models.Model):
    """
    Requirments model
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class BadgeRequest(models.Model):
    """
    BadgeRequest model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Badge Request"

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.approved:
            self.user.badges.add(self.badge)
            self.user.save()
            self.user.email_user(
                subject='Badge Approved',
                message=f'You have been approved for the {self.badge.name} badge.',
            )
        super().save(*args, **kwargs)



class Donation(models.Model):
    """
    Donation model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    stripe_charge_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-date"]


class DonationProof(models.Model):
    """
    Donation Proof model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True, blank=True)
    proof = models.FileField(storage=gd_storage)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Donation Proof"

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.approved:
            Donation.objects.create(user=self.user, amount=self.amount, stripe_charge_id='Others')
            self.user.email_user(
                subject='Donation Confirmation',
                message=f'Your donation of Rs.{self.amount} has been approved!\nThank you for your donation!\n\n- The Vitary Team',
            )
        super().save(*args, **kwargs)
