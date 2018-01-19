from models import Model
import time

Model = Model


class Reply(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('content', str, ''),
            ('topic_id', str, 0),
            ('user_id', str, 0),
        ]
        return names

    def user(self):
        from .user import User
        u = User.one(id=self.user_id)
        return u

    def pub_time(self):
        t_int = int(self.created_time)
        local_time= time.localtime(t_int)
        format = '%Y-%m-%d %H:%M:%S'
        t = time.strftime(format, local_time )
        return t