from users.models import Notifications


def notification_context(request):
    if request.user.is_anonymous:
        return {}

    n = Notifications.objects.filter(recipient=request.user).order_by('-timestamp')

    return {
        'notification': n,
    }