from django.db import models
from django.utils.text import slugify

# Lists of choices
GENDER = ((0, "Male"), (1, "Female"), (2, "Other"))


# Create model for customer
class Customer(models.Model):
    """Creates a model for customers.

    Args:
        models: The base model class.

    Attributes:
        id (int): The unique identifier for the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        address (str): The address of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
        information (str): Additional information about the customer.
        created_on (datetime): The date and time when the customer was created.
        updated_on (datetime): The date and time when the customer was updated.
        ___str___: Returns the full name of the customer.
    """

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
        ordering = ["last_name"]

    # Returns the full name of the customer
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# Create model for guest
class Guest(models.Model):
    """
    Creates a model for guests.

    Args:
        models: The base model class.

    Attributes:
        id (AutoField): The primary key for the guest.
        first_name (CharField): The first name of the guest.
        last_name (CharField): The last name of the guest.
        name_addon (CharField): An additional name for the guest.
        gender (IntegerField): The gender of the guest.
        image (ImageField): An image of the guest.
        date_of_birth (DateField): The date of birth of the guest.
        information (TextField): Additional information about the guest.
        food (BooleanField): Indicates if the guest requires food.
        food_time_1 (TimeField): The first food time for the guest.
        food_time_2 (TimeField): The second food time.
        food_time_3 (TimeField): The third food time.
        medication (BooleanField): Indicates if the guest requires medication.
        medication_time_1 (TimeField): The first medication time for the guest.
        medication_time_2 (TimeField): The second medication time.
        medication_time_3 (TimeField): The third medication time.
        created_on (DateTimeField): The date and time the guest was created.
        updated_on (DateTimeField): The date and time the guest was updated.
        customer_id (ForeignKey): The foreign key to the associated customer.
        slug (SlugField): A unique slug for the guest.

    Methods:
        save: Overrides the save method to automatically
            generate a slug for the guest.
        get_gender: Translates the gender coding to categories.
        get_last_name: Returns the last name of the guest.
        __str__: Returns a string representation of the guest.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    name_addon = models.CharField(max_length=50, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date_of_birth = models.DateField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
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
        ordering = ["first_name"]

    # Automatically creates a slug for the guest
    # by combining first_name and name_addon
    def save(self, *args, **kwargs):
        if not self.slug:
            if self.name_addon is None:
                self.slug = slugify(self.first_name)
            else:
                self.slug = slugify(f"{self.first_name}-{self.name_addon}")
        super().save(*args, **kwargs)

    # Translates gender coding to categories
    def get_gender(self):
        if self.gender == 0:
            return "Male"
        elif self.gender == 1:
            return "Female"
        elif self.gender == 2:
            return "Other"
        else:
            return "Not defined"

    # Returns the full name of the guest
    def get_last_name(self):
        if self.last_name is None:
            return ""
        else:
            return self.last_name

    # Returns all necessary information about the guest
    def __str__(self):
        return (
            f"{self.first_name} {self.get_last_name()} "
            f"({self.name_addon}) {self.get_gender()}"
        )


# Create model for tracking guest presence
class Presence(models.Model):
    """
    Returns a string representation of the Presence model.

    Returns:
        str: A string containing the date, check-in time,
            check-out time, guest's first name,
            last name, ID, and pickup name.
    """

    id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    pickup_name = models.CharField(max_length=50, null=True, blank=True)

    # Only one entry of the combination of guest and date allowed
    class Meta:
        unique_together = ("guest", "date")

    # Return all necessary information about the presence of a guest
    def __str__(self):
        return (
            f"{self.date} {self.check_in} "
            f"{self.check_out} {self.guest.first_name} "
            f"{self.guest.last_name} {self.guest.id} "
            f"{self.pickup_name}"
        )
