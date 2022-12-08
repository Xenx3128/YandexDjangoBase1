import datetime

from users.models import User


def birthdays(request):
    today = datetime.date.today()
    birthdays = User.objects.filter(birthday__lte=today)
    return {
        'birth_users': birthdays,
    }
