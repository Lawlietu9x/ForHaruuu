# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserReg(models.Model):
    """A form that can user Sign up."""
    Frist_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=254)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the text and email field."""
        return self.text
