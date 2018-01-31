论坛功能
--------

1. 上传头像
2. 私信和AT
3. 导航栏和 jinja2 模板继承



上传头像
--------
1. form
2. post方法 对应一个路由 保存静态文件的功能
    1. 文件后缀要做过滤 img png gif
    2. 文件名也要小心
    ../../home/akirayu/.bash_rc -> xxxxxx
    ~/.bash_rc
    ~/.bash_profile
3. get方法，本地的静态文件转发给用户


发私信 数据结构
--------------
1. id
2. content
3. title
4. sender_id # 这个不应该是从表单里面拿的，hidden，伪造成任何人
5. receiver_id


切换到 mongo
------------

1. 增删改查
2. id
3. deleted

部署
----
- nginx : web server
- gunicorn: application server
- wsgi: 包装出来一个app
- request -> nginx -> gunicorn -> wsgi -> app(Flask) -> route

1. 反向代理
    - gunicorn 2000
    - nginx 80
2. 负载均衡
    - gunicorn worker
3. 静态文件托管
    - send_by_directory 每次都 send 很不好
    - 配置了一个规则，保存在 nginx 的缓存，不会走到 app 这一层

4. redis
    - 缓存
    - 共享数据


# 1.注册 登录 退出
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E6%B3%A8%E5%86%8C%E7%99%BB%E5%BD%95%E9%80%80%E5%87%BA.gif)

# 2.设置个人信息（个性签名 / 更改密码 / 更换头像）
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E8%AE%BE%E7%BD%AE%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.gif)

# 3.发表文章、添加评论（都支持markdown及语法高亮）
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E5%8F%91%E5%B8%83%E8%AF%9D%E9%A2%98%E3%80%81%E6%B7%BB%E5%8A%A0%E8%AF%84%E8%AE%BA.gif)

# 4.邮件收发功能
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E9%82%AE%E4%BB%B6%E6%94%B6%E5%8F%91%E5%8A%9F%E8%83%BD.gif)

#5.板块功能（增加板块，查看板块所属文章）
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E5%A2%9E%E5%8A%A0%E6%9D%BF%E5%9D%97%E3%80%81%E6%9F%A5%E7%9C%8B%E5%90%84%E6%9D%BF%E5%9D%97%E6%96%87%E7%AB%A0.gif)

# 6.个人信息（更换头像、查看发布的话题和评论的话题）
![img](https://github.com/majunjun12345/forum/blob/master/%E9%A1%B5%E9%9D%A2%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D/%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF.gif)

# 7.评论区的 @ 功能
