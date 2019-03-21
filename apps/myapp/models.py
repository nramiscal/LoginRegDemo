from django.db import models

class UserManager(models.Manager):
    def reg_validator(self, form):

        errors = {}

        fname = form['fname']
        lname = form['lname']
        email = form['email']
        password = form['password']
        confirm_pw = form['confirm_password']

        if len(fname) < 2:
            errors['fname'] = "First name cannot be blank"
        if len(lname) < 2:
            errors['lname'] = "Last name cannot be blank"
        if len(email) < 1:
            errors['email'] = "Email cannot be blank"
        # also check if valid email format :)
        else:
            users = User.objects.filter(email=email)
            if len(users) > 0:
                errors['email'] = "Email already exists. Please login."
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif password != confirm_pw:
            errors['confirm_pw'] = "Passwords do not match"

        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

"""
models come with a hidden property:
      objects = models.Manager()
we are going to override this!
"""
