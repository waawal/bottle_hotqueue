# bottle_hotqueue

FIFO messagequeue plugin for Bottle based on _HotQueue_

## Installation

    $ sudo pip install bottle_hotqueue

From source:

    $ sudo python setup.py install

Dependencies:

    bottle, hotqueue

## Getting Started
```python
import bottle
from bottle_hotqueue import HotQueuePlugin


app = bottle.Bottle()
hotqueue = HotQueuePlugin(keyword="queue", prefix="bottle")
app.install(hotqueue)


@app.get('/add/:value', queue={'key': 'testkey'})
def send_message(value, testkey):
    """ This will put an item in the queue bottle:testkey.
    """
    return testkey.put(value)


@app.get('/', queue={'key': 'testkey'})
def get_message(testkey):
    """ We will now try to get a item from bottle:testkey.
        if the queue is empy, we instead raise a 404.
    """
    result = testkey.get()
    if not result:
        raise bottle.HTTPError(404, "Queue is Empty")
    return result

bottle.run(app, host='', port=8080)
```