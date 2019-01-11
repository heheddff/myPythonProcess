from celery.task import Task
import time


class CourseTask(Task):
    name = 'course-task'

    def run(self):
        print('start course task')
        time.sleep(6)
        print('end course task')