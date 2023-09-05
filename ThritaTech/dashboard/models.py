from django.db import models
from django.utils import timezone
import datetime


class CalendarItem(models.Model):
    calendar = models.ForeignKey("Calendar", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self) -> str:
        # show the owner's username and number of items
        return f"{self.owner.username} ({self.calendaritem_set.count()})"

    def __repr__(self) -> str:
        return self.__str__()

    def get_items(self, now=None):
        if now is None:
            now = timezone.now()
        return self.calendaritem_set.filter(end__gte=now)

    # seperate items by day and return a dict containing the items
    def get_items_by_day(self, now=None):
        if now is None:
            now = timezone.now()
        items = self.get_items(now)
        days = {}
        for item in items:
            day = item.start.date()
            if day not in days:
                days[day] = []
            days[day].append(item)
        return days
