from models import Model
from models.user import User

import time

class Topic(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('views', int, 0),
            ('title', str, ''),
            ('content', str, ''),
            ('user_id', str, 0),
            ('board_id', str, 0),
        ]
        return names

    @classmethod
    def find(cls, id):
        m = cls.one(id=id)
        m.views += 1
        m.save()
        return m

    def replies(self):
        from .reply import Reply
        ms = Reply.all(topic_id=self.id)
        return ms

    def board(self):
        from .board import Board
        m = Board.one(id=self.board_id)
        return m

    def user(self):
        u = User.one(id=self.user_id)
        return u

    def pub_time(self):
        t_int = int(self.created_time)
        local_time= time.localtime(t_int)
        format = '%Y-%m-%d %H:%M:%S'
        t = time.strftime(format, local_time )
        return t