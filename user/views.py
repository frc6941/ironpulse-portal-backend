from django.http import JsonResponse

from activity.models import Activity
from user.forms import GetUserByName, GetUserByToken, SignIn
from user.models import user_to_dict, User, users_to_dict


def get_user_by_name(request, name):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    form = GetUserByName({'name': name})

    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse(
        user_to_dict(User.objects.get(name=form.clean_name())),
        status=200
    )


def get_user_by_token(request, token):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    form = GetUserByToken({'token': token})

    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse(
        user_to_dict(User.objects.get(token=form.clean_token())),
        status=200
    )


def get_all_users(request):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    return users_to_dict(User.objects.all())


def sign_in(request, token, activity_id):
    if request.method != 'GET':
        return JsonResponse({}, status=405)

    form = SignIn({'token': token, 'activity_id': activity_id})

    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    user = User.objects.get(token=form.clean_token())
    activity = Activity.objects.get(id=form.clean_activity_id())

    user.taken_activities.add(activity)

    return JsonResponse({}, status=200)
