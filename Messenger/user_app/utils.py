from django.contrib.auth import get_user_model

User = get_user_model()

def email_authenticate(email: str, password: str):

    user = User.objects.filter(email = email)
    print("??")
    if len(user) > 0:
        print("user here")
        if user[0].check_password(password):
            print("good pass")
            return user[0]
    return None 
