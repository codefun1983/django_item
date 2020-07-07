import os
import time
from celery import shared_task

@shared_task
def ppop(a,b):
    xyz = [a, b]
    time.sleep(180)
    for i in range(2):
        for yz in xyz:
            os.system('rm -rvf %s*' % yz)
