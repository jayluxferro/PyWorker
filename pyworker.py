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
