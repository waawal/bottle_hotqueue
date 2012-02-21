import inspect
from functools import wraps
try:
    import simplejson as json
except ImportError:
    import json
import hotqueue
import redis

class HotQueuePlugin(object):
    name = 'hotqueue'
    api = 2

    def __init__(self, host='localhost', port=6379, database=0,
                 keyword='queue', asjson=True, prefix="hotqueue"):
        self.keyword = keyword
        if asjson:
            self.asjson = json
        else:
            self.asjson = asjson or None
        hotqueue.key_for_name = lambda x: ''.join([prefix, ":", x])
        self.host = host
        self.port = port
        self.database = database
        
    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, HotQueuePlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another hotqueue plugin with "\
                        "conflicting settings (non-unique keyword).")
            self.redispool = redis.ConnectionPool(host=self.host,
                                               port=self.port, db=self.database)


    def apply(self, callback, route):
        conf = route.config.get(self.keyword) or {}
        if not conf or not 'queue' in conf:
            return callback
        else:
            keyword = conf['queue']
        args = inspect.getargspec(callback)[0]
        if keyword not in args:
            return callback

        @wraps(callback)
        def wrapper(*args, **kwargs):
            queue = hotqueue.HotQueue(keyword, serializer=self.asjson,
                                      connection_pool=self.redispool)
            kwargs[keyword] = queue
            return callback(*args, **kwargs)
        return wrapper

Plugin = HotQueuePlugin
