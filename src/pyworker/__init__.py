r"""PyWorker is a simple implementation of a worker-pool process.

Example:

from pyworker import PyWorker
from time import time

def some_task(item):
    print(item)

task_items = []
for t in range(10 * 6):
    task_items.append(t)

worker = PyWorker()

start = time()
# run the tasks
worker.run(some_task, task_items, worker_pool=100)

# wait till all the tasks complete
worker.wait()

# stop all threads
worker.stop()

print('Task completed in {} seconds'.format(time() - start))
"""
__version__ = '1.0.0'
__all__ = [
    'threading', 'queue', 'time', 'sleep'
]

__author__ = 'Jay <jay@sperixlabs.org>'

import threading
import queue
from time import sleep

class PyWorker():
    def __init__(self):
        self.q = queue.Queue()
        self.threads = []

    def enqueue(self, task_items):
        for item in task_items:
            self.q.put(item)

    def run(self, task, task_items, worker_pool=1):
        self.worker_pool = worker_pool
        for i in range(self.worker_pool):
            t = threading.Thread(target=self.worker, args=(task,))
            t.start()
            self.threads.append(t)

        # queue task items
        self.enqueue(task_items)

    def worker(self, task):
        while True:
            item = self.q.get()
            if item is None:
                break
            task(item)
            sleep(1)
            self.q.task_done()

    def wait(self):
        # Block until all tasks are complete
        self.q.join()

    def stop(self):
        # stop the workers
        self.stop_workers()

    def stop_workers(self):
        # stop workers
        for i in self.threads:
            self.q.put(None)
        for t in self.threads:
            t.join()
