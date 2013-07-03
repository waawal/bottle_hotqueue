bottlehotqueue
==============

*FIFO message queue* plugin for **bottle.py** based on **HotQueue**

`bottle.py <http://bottlepy.org>`_ is a fast and simple micro-framework for python web-applications.

`HotQueue <https://richardhenry.github.com/hotqueue/>`_ is a Python library that allows you to use Redis as a message queue within your Python programs.

Installation
------------
::

    $ pip install bottle-hotqueue

From source
***********
::

    $ python setup.py install

Dependencies
************

`bottle` and `hotqueue`

Getting Started
---------------

Importing and using the plugin in Bottle
****************************************
::

    import bottle
    from bottlehotqueue import Plugin


    app = bottle.Bottle()
    hotqueue = Plugin(keyword="myhotqueue")
    app.install(hotqueue)


    @app.post('/put/:value', myhotqueue={'queue': 'myqueue'})
    def send_message(value, myqueue):
        """ This will put an item in the queue hotqueue:myqueue.
        """
        return myqueue.put(value)


    @app.get('/get/', myhotqueue={'queue': 'myqueue'})
    def get_message(myqueue):
        """ We will now try to get a item from hotqueue:myqueue.
            if the queue is empty, we instead raise a 404.
        """
        result = myqueue.get()
        if not result:
            raise bottle.HTTPError(404, "Queue is Empty")
        return result

    bottle.run(app, host='', port=8080)


The plugin will use `json` (or simplejson if available) as the standard serializer. This behaviour can be reverted to match the default implementation by passing asjson=False when instantiating the plugin. It will then conform to the standard HotQueue way of serializing objects by using pickle (or cpickle if available).

::

    hotqueue = Plugin(keyword="myhotqueue", asjson=False)

Writing a simple consumer
*************************
::

    import json
    from hotqueue import HotQueue


    queue = HotQueue("myqueue", host="localhost", serializer=json)

    for item in queue.consume():
        print item


More on HotQueue: http://richardhenry.github.com/hotqueue/

License
-------
MIT

Github links
  * https://github.com/defnull/bottle
  * https://github.com/richardhenry/hotqueue
