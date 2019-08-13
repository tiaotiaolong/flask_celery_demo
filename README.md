# flask_celery_demo
一个基于flask celery的可运行的demo，用于备忘

利用redis做中间件，首先安装redis

```
brew install redis
```

启动celery work

```
papapa_venv/bin/celery worker -A run.celery --loglevel=info

```

pycharm 启动项目

访问localhost:5000/celeryapp/test

调用异步任务,下图说明任务已经启动

![](http://tiaogithub.cn-bj.ufileos.com/flask_celery_01.jpg)





