from django.db import models
import string
import random
# Create your models here. put more models for max logic constraints

# generate unique code to join room


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        #
        # check if the code is unique
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    # adding constrains to the Room class
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)  # join code
    # information about the host
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
