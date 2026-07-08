fromdjango.contrib.authimportget_user_model
DEFAULT_USERS = (
    {"username":"admin","password":"admin123","role":"ADMIN","is_staff":True,"is_superuser":True},
    {"username":"marketing","password":"marketing123","role":"MARKETING","is_staff":False,"is_superuser":False},
    {"username":"sales","password":"sales123","role":"SALES","is_staff":False,"is_superuser":False},
)
defcreate_default_users(**kwargs):
    User=get_user_model()
    foraccountinDEFAULT_USERS:
        user,created=User.objects.get_or_create(username=account["username"])
        user.role=account["role"]
        user.is_staff=account["is_staff"]
        user.is_superuser=account["is_superuser"]
        ifcreated:
            user.set_password(account["password"])
        user.save()
