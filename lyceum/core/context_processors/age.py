import datetime

from users.models import User


def birthdays(request):
    list = []
    for user in User.objects.all():
        if user.birthday:
            birthday = user.birthday.strftime('%b %d')
            today = datetime.date.today().strftime('%b %d')
            if birthday == today:
                list.append(user)
    return {
        'birth_users': list,
    }
