from django.contrib.auth.hashers import check_password, make_password
from .models import Gruser
import logging
 
 
class MyAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            print('came here')
            user = Gruser.objects.get(username__exact=username)
            if check_password(password, make_password(user.password)):
                print('checked')
                return user
            else:
                print('not checked')
                return None
        except Gruser.DoesNotExist:
            logging.getLogger("error_logger").error("user with username %s does not exists " % username)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = Gruser.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except Gruser.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None