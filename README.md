# bottle_hotqueue

_FIFO message queue_ plugin for _bottle.py_ based on _HotQueue_

_[bottle.py](http://bottlepy.org) is a fast and simple micro-framework for python web-applications._

_[HotQueue](http://richardhenry.github.com/hotqueue/) is a Python library that allows you to use Redis as a message queue within your Python programs._

## Installation

    $ sudo pip install bottle_hotqueue

### From source:

    $ sudo python setup.py install

### Dependencies:

    bottle, hotqueue

## Getting Started

### Importing and using the plugin in Bottle

```python
import bottle
from bottle_hotqueue import HotQueuePlugin


app = bottle.Bottle()
hotqueue = HotQueuePlugin(keyword="myhotqueue")
app.install(hotqueue)


@app.get('/add/:value', myhotqueue={'queue': 'myqueue'})
def send_message(value, myqueue):
    """ This will put an item in the queue hotqueue:myqueue.
    """
    return myqueue.put(value)


@app.get('/', myhotqueue={'queue': 'myqueue'})
def get_message(myqueue):
    """ We will now try to get a item from hotqueue:myqueue.
        if the queue is empty, we instead raise a 404.
    """
    result = myqueue.get()
    if not result:
        raise bottle.HTTPError(404, "Queue is Empty")
    return result

bottle.run(app, host='', port=8080)
```

The plugin will use json (or simplejson if available) as the standard serializer. This behaviour can be reverted by passing asjson=False when instantiating the plugin. It will then conform to the standard HotQueue way of serializing objects by using pickle (or cpickle if available).

```python
hotqueue = HotQueuePlugin(keyword="myhotqueue", asjson=False)
```

### Writing a simple consumer

```python
import json
from hotqueue import HotQueue


queue = HotQueue("myqueue", host="localhost", serializer=json)

for item in queue.consume():
    print item

```
More on HotQueue: http://richardhenry.github.com/hotqueue/

### License
MIT

### Github links
* https://github.com/defnull/bottle
* https://github.com/richardhenry/hotqueue