#!/usr/bin/env python

import os

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
secret = get_random_string(50, chars)

with open(os.path.join(os.path.dirname(__file__), 'secret_key'), 'w') as f:
    f.write(secret)
