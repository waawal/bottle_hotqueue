import inspect
try:
    import simplejson as json
except ImportError:
    import json
import hotqueue


class HotQueuePlugin(object):
    name = 'hotqueue'
    api = 2

    def __init__(self, host='localhost', port=6379, database=0,
                 keyword='queue', asjson=True, prefix="hotqueue"):
        self.host = host
        self.port = port
        self.database = database
        self.keyword = keyword
        if asjson:
            self.asjson = json
        else:
            self.asjson = None
        hotqueue.key_for_name = lambda x: ''.join([prefix, ":", x])

    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, HotQueuePlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another hotqueue plugin with "\
                        "conflicting settings (non-unique keyword).")

    def apply(self, callback, route):
        conf = route.config.get(self.keyword) or {}
        keyword = conf.get('queue')
        args = inspect.getargspec(callback)[0]
        if keyword not in args or self.keyword in route.skiplist:
            return callback

        def wrapper(*args, **kwargs):
            queue = hotqueue.HotQueue(keyword, host=self.host,
                                       port=self.port, db=self.database,
                                       serializer=self.asjson)

            kwargs[keyword] = queue
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

Plugin = HotQueuePlugin
