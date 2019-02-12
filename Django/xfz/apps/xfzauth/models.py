
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models

class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请传入手机号码')
        if not username:
            raise ValueError('请传入用户名')
        if not password:
            raise ValueError('请传入密码')

        user = self.models(telephone=telephone, username=username, **kwargs)
        user.get_password(password)
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone,username,password,**kwargs)

    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone,username,password,**kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    # 我们不使用默认的自增长的主键
    # UUID/shortuuid：
    # shortuuid：pip install django-shortuuidfield, 在import时 import shortuuidfield
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(unique=True,max_length=11)
    email = models.CharField(unique=True,max_length=255)
    username = models.CharField(max_length=100)
    is_active = models.CharField(default=True,max_length=2)
    is_staff = models.BooleanField(default=True)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'  # 注意若不重写，则默认用username来验证
    # telephone,username,password
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

