from django.db import models
from django.utils import timezone
import datetime


class CalendarItem(models.Model):
    calendar = models.ForeignKey("Calendar", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    link = models.URLField()
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=7, default="#007bff")

    def __unicode__(self):
        return self.title

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title

    def is_active(self, now):
        return self.start <= now and self.end >= now

    def is_ended(self, now):
        return self.end < now

    def is_upcoming(self, now):
        return self.start > now

    def is_current(self, now):
        return self.start <= now and self.end >= now

    def is_today(self, now):
        return self.start.date() == now.date()


class Calendar(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title

    def today(self):
        return self.items.filter(start__date=datetime.date.today())

    def get_day(self, day):
        return self.items.filter(start__date=day)

    def seperate_by_day(self, items):
        days = {}
        for item in items:
            day = item.start.date()
            if day in days:
                days[day].append(item)
            else:
                days[day] = [item]
        return days
