#!/usr/bin/env python
"""
Django SECRET_KEY generator.
"""
import random


def generate_secret_key(lenght=50):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(random.choice(chars) for i in range(lenght))


print(generate_secret_key())
