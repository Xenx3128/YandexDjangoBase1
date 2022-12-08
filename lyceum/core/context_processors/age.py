import datetime

from users.models import User


def birthdays(request):
    today = datetime.date.today()
    birthdays = User.objects.filter(birthday__lte=today)

    # list = [user for user in User.objects.all()
    #         if user.birthday.strftime('%b %d') ==
    #         datetime.date.today().strftime('%b %d')]
    return {
        'birth_users': birthdays,
    }
