from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import EmplopyeeDetails

def employee_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='employees')
		instance.groups.add(group)
		EmplopyeeDetails.objects.create(
			user=instance,
			employee_name=instance.username,
			)
		print('Profile created!')

post_save.connect(employee_profile, sender=User)

