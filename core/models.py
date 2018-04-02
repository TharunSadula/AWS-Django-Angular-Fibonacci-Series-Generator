# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Fibonacci(models.Model):
    num = models.IntegerField(null=True, blank=True)
    fib = models.CharField(max_length=255)

    def __str__(self):
            return "Fib: {}".format(self.num, self.fib)
