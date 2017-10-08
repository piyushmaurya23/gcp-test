# -*- coding: utf-8 -*-
"""
This module is a standard Django generated views module for custom application
"""

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Domain(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    is_licensed = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    is_licensed = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
