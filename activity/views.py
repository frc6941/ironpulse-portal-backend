from django.http import JsonResponse

from activity.models import Activity, activity_to_dict, activities_to_dict
from user.forms import GetUserByToken
from user.models import User


def create_activity(request, token):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    form = GetUserByToken({'token': token})

    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    user = User.objects.get(token=token)

    if user.role != 'ADMIN':
        return JsonResponse({}, status=401)

    activity = Activity.objects.create()

    return JsonResponse(
        activity_to_dict(activity),
        status=200
    )


def get_all_activities(request):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    return activities_to_dict(Activity.objects.all())
