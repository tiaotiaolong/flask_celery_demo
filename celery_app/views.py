from flask import Blueprint
from .tasks import celery_task


celery_bp = Blueprint("domain", __name__, url_prefix='/celeryapp')


@celery_bp.route('/test')
def test():
    celery_task.delay()
    return 'a'