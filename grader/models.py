from django.db import models


class TimeLog(models.Model):
    urs = models.CharField(blank=True, max_length=45)
    activity = models.CharField(max_length=30)
    duration = models.DurationField(blank=True, null=True)  # datetime.timedelta
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
