from django.http import Http404

from custom_user.models import IgnoreUser


def remove_user_from_ignore(request):
    try:
        qs = IgnoreUser.objects.get(user=request.user.id, ignored_user=request.data['ignored_user'])
        qs.ignore = False
        qs.save()
    except:
        raise Http404