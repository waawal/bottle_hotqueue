import inspect
try:
    import simplejson as json
    jsonavailable = True
except ImportError:
    jsonavailable = False
import hotqueue


class HotQueuePlugin(object):
    name = 'hotqueue'

    def __init__(self, host='localhost', port=6379, database=0,
                 keyword='queue', asjson=True, prefix="bottle"):
        self.host = host
        self.port = port
        self.database = database
        self.keyword = keyword
        if asjson and jsonavailable:
            self.asjson = json
        else:
            self.asjson = None
        hotqueue.key_for_name = lambda x: prefix + ":" + x

    def setup(self, app):
        for other in app.plugins:
            if not isinstance(other, HotQueuePlugin):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another hotqueue plugin with "\
                        "conflicting settings (non-unique keyword).")

        self.queue = hotqueue.HotQueue(self.keyword, host=self.host,
                                       port=self.port, db=self.database,
                                       serializer=self.asjson)

    def apply(self, callback, context):
        args = inspect.getargspec(context['callback'])[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = self.queue
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

Plugin = HotQueuePlugin
