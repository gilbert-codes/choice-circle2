import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choice_site.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
u = User.objects.get(username="admin")
u.set_password("Gilbert$123")
u.save()
print("Admin password reset to: Gilbert$123")
