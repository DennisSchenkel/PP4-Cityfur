from django.db import models
from guests.models import Guest


# Create your models for report
class Report(models.Model):
    """
    Represents a report.

    Args:
        models: The base model class.

    Attributes:
        id (AutoField): The primary key for the report.
        report_date (DateField): The date of the report.
        report_text (TextField): The text content of the report.
        created_on (DateTimeField): The date and time when the
            report was created.
        updated_on (DateTimeField): The date and time when the
            report was last updated.
        guests (ManyToManyField): The guests associated with the report.

    Meta:
        ordering (list): The default ordering for the reports based
            on the report date.

    Methods:
        __str__(): Returns a string representation of the report.

    """

    id = models.AutoField(primary_key=True)
    report_date = models.DateField(null=False)
    report_text = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    guests = models.ManyToManyField(Guest, related_name='reports', blank=True)

    class Meta:
        ordering = ['report_date']

    def __str__(self):
        return f'{self.report_date} <br> {self.report_text}'
