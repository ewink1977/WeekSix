from django.db import models
import re, datetime
from datetime import date, datetime

# Thanks, StackOverflow!
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class ValidationTest(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors['firstname'] = "First name must be more than two characters."
        if len(postData['lastname']) < 2:
            errors['lastname'] = "Last name must be more than two characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        # Magic to make the date comparison work.
        dateentered = postData['birthdate']
        birthdate = datetime.strptime(dateentered, "%Y-%m-%d")
        today = datetime.now()
        if birthdate >= today:
            errors['birthdate'] = "You're not a time traveler. Your birthdate must be in the past."
        elif calculate_age(birthdate) < 13:
            errors['birthdate'] = "You must be at least 13 years old to sign up for this website."
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters."
        if not postData['confirm-pw'] == postData['password']:
            errors['confirm-pw'] = "Password mismatch. Maybe a typo? Please try again!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
    objects = ValidationTest()
