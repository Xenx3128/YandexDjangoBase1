import datetime

from users.models import User


def birthdays(request):
    list = [user for user in User.objects.all()
            if user.birthday.strftime('%b %d') ==
            datetime.date.today().strftime('%b %d')]
    return {
        'birth_users': list,
    }
