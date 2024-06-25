from django.db import models

# Create your models for report
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    report_date = models.DateField(null=False)
    report_text = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['report_date']
    
    def __str__(self):
        return f'{self.report_date} <br> {self.report_text}'