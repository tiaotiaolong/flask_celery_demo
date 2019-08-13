from flask import Flask
from celery_app import celery


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app.config)

    # 添加蓝本
    from celery_app.views import celery_bp
    app.register_blueprint(celery_bp)

    return app


def make_celery(app):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
