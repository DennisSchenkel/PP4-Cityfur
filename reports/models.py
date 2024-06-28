from django.db import models
from guests.models import Guest

# Create your models for report
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    report_date = models.DateField(null=False)
    report_text = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    guests = models.ManyToManyField(Guest, related_name='reports')

    
    class Meta:
        ordering = ['report_date']
    
    def __str__(self):
        return f'{self.report_date} <br> {self.report_text}'
    
    
# Create your models for mentioned guests
class MentionedGuest(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['report_id']
        
    def __str__(self):
        return f'{self.report} <br> {self.guest}'