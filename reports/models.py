from django.db import models
from guests.models import Guest

# Create your models for report
class Report(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
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
    
    