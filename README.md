## PyWorker
PyWorker is a simple implementation of a worker-pool process.

### Installation

```
pip install git+https://github.com/jayluxferro/PyWorker
```


### Test Implementation
```python
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
```
