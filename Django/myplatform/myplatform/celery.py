from __future__ import absolute_import, unicode_literals   #这句导入一定要在第一的位置
import os
from celery import Celery
from django.conf import settings

#这里我们的项目名称为,所以为platform.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myplatform.settings")

# 创建celery应用
app = Celery('dailyblog')
#doesn’t have to serialize the object.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
