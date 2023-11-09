import uuid
from typing import List, Dict, Any

from django.db import models


class User(models.Model):
    USER_ROLES = [
        ('STUDENT', 'Student'),
        ('ADMIN', 'Admin')
    ]

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    token = models.UUIDField(editable=False, unique=True)
    role = models.CharField(choices=USER_ROLES)
    taken_activities = models.ManyToManyField('Activity')


def user_to_dict(user: User) -> Dict[str, Any]:
    return {
        'id': user.id,
        'name': user.name,
        'token': user.token
    }


def users_to_dict(users: List[User]) -> List[Dict[str, Any]]:
    return [user_to_dict(user) for user in users]
