from typing import Dict, Any, List

from django.db import models


class Activity(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    date = models.DateField(auto_now_add=True)


def activity_to_dict(activity: Activity) -> Dict[str, Any]:
    return {
        'id': activity.id,
        'date': activity.date.strftime('%Y/%m/%d %H:%M:%S')
    }


def activities_to_dict(activities: List[Activity]) -> List[Dict[str, Any]]:
    return [activity_to_dict(activity) for activity in activities]
