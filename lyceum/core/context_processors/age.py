import datetime

from users.models import User


def birthdays(request):
    bday_users = []
    for user in User.objects.all():
        if user.birthday:
            birthday = user.birthday.strftime('%b %d')
            today = datetime.date.today().strftime('%b %d')
            if birthday == today:
                bday_users.append(user)
    return {
        'birth_users': bday_users,
    }
