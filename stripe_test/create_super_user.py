import os
import argparse

import django
from dotenv import dotenv_values

parser = argparse.ArgumentParser(description='Create superuser.')
parser.add_argument('user', type=str)
parser.add_argument('password', type=str)

args = parser.parse_args()

os.environ['DJANGO_SETTINGS_MODULE'] = 'stripe_test.settings'
django.setup()

from django.contrib.auth.models import User


def create_superuser(username, password):
    user = User.objects.create_superuser(
        username=username,
        password=password
    )
    user.is_active = True
    user.save()


if __name__ == "__main__":
    try:
        create_superuser(args.user, args.password)
    except Exception as err:
        print(err)
