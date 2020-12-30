from django.db import models
import re

class ValidationTest(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than two characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be more than two characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    objects = ValidationTest()
