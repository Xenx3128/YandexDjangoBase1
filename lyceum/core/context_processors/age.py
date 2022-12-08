from users.models import User
import datetime


def birthdays(request):
    list = [user for user in User.objects.all() if user.birthday.strftime('%b %d') == datetime.date.today().strftime('%b %d')]
    print('#####################################################################################')
    print(list)
    return {
        'birth_users': list,
    }
