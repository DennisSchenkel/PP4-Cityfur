from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Lists of choices
GENDER = ((0, 'Male'), (1, 'Female'), (2, 'Other'))

# Create model for customer
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    # Orders customers by last name
    class Meta:
        ordering = ['last_name']
    
    # Returns the full name of the customer
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    

# Create model for guest
class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    name_addon = models.CharField(max_length=50, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    date_of_birth = models.DateField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    picture_url = models.URLField(null=True, blank=True)
    food = models.BooleanField(default=False)
    food_time_1 = models.TimeField(null=True, blank=True)
    food_time_2 = models.TimeField(null=True, blank=True)
    food_time_3 = models.TimeField(null=True, blank=True)
    medication = models.BooleanField(default=False)
    medication_time_1 = models.TimeField(null=True, blank=True)
    medication_time_2 = models.TimeField(null=True, blank=True)
    medication_time_3 = models.TimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # Orders guests by first name
    class Meta:
        ordering = ['first_name']   

    # Automatically creates a slug for the guest by combining first_name and name_addon
    def save(self, *args, **kwargs):
        if not self.slug:
            if self.name_addon == None:
                self.slug = slugify(self.first_name)
            else:
                self.slug = slugify(f"{self.first_name}-{self.name_addon}")
        super().save(*args, **kwargs)
    
    # Translates gender coding to categories
    def get_gender(self):
        if self.gender == 0:
            return 'Male'
        elif self.gender == 1:
            return 'Female'
        elif self.gender == 2: 
            return 'Other'
        else:
            return 'Not defined'
    
    # Returns the full name of the guest
    def get_last_name(self):
        if self.last_name == None:
            return ''
        else:
            return self.last_name
    
    # Returns all necessary information about the guest
    def __str__(self):
        return f'{self.first_name} {self.get_last_name()} ({self.name_addon}) {self.get_gender()}'
    
    
# Create model for tracking guest presence
class Presence(models.Model):
    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)

    # Only one entry of the combination of guest and date allowed
    class Meta:
        unique_together = ('guest', 'date')  

    # Return all necessary information about the presence of a guest
    def __str__(self):
        return f"{self.date} {self.check_in} {self.check_out} {self.guest.first_name} {self.guest.last_name} {self.guest.id}"