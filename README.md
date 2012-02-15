# bottle_hotqueue

FIFO messagequeue plugin for Bottle based on _HotQueue_

## Installation

    $ sudo pip install bottle_hotqueue

From source:

    $ sudo python setup.py install

## Getting Started

    from bottle_hotqueue import Plugin


    app = bottle.Bottle()
    hotqueue = Plugin(keyword="q")
    app.install(hotqueue)


    @app.post('/:value')
    def send_message(q, value):
        return q.put(value)


    @app.get('/')
    def get_message(q):
        result = q.get()
        if not result:
            raise bottle.HTTPError(404, "Queue is Empty")
        return result

    bottle.run(app, host='', port=8080)
