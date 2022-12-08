import datetime

from users.models import User


def birthdays(request):
    day, month = datetime.date.today().day, datetime.date.today().month
    birthdays = User.objects.filter(birthday__day=day, birthday__month=month)

    return {
        'birth_users': birthdays,
    }
