# from models import Model
from models import Model
import models

Model = Model


class User(Model):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """

    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('username', str, ''),
            ('password', str, ''),
            ('personalized_signature', str, ''),
            ('user_image', str, '/uploads/default.png'),
        ]
        return names

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    def hashed_password(self, pwd):
        import hashlib
        # 用 ascii 编码转换成 bytes 对象
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        name = form['username']
        password = form['password']
        if len(name) > 2 and User.one(username=name) is None:
            password = User.salted_password(password)
            u = User.new(dict(
                username=name,
                password=password,
            ))
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        user = User.one(
            username=form['username'],
            password=User.salted_password(form['password'])
        )
        return user

    # 用 类方法，不用实例化，可以直接调用
    @classmethod
    def topics(cls, id):
        topics = models.topic.Topic.all(user_id=id)
        return sorted(topics, key= lambda topic: topic.created_time, reverse=True)

    @classmethod
    def replied_topics(cls, id):
        replies = models.reply.Reply.all(user_id=id)
        topic_ids = []
        replied_topics = []
        for reply in replies:
            topic_id = reply.topic_id
            topic_ids.append(topic_id)
        # 避免同一话题下多次回复，陈列多次相同主体
        for id in set(topic_ids):
            topic = models.topic.Topic.one(id=id)
            replied_topics.append(topic)
        # print('replied_topics:', replied_topics)
        if None in replied_topics:
            # remove() 方法没有返回值
            # replied_topics = replied_topics.remove(None)
            # 所以 replied_topics 为 None
            replied_topics.remove(None)
        # print('replied_topics:no None',replied_topics)
        return sorted(replied_topics, key= lambda topic: topic.created_time, reverse=True)