import unittest
import os
import bottle
import hotqueue
from bottlehotqueue import Plugin

class HotQueueTest(unittest.TestCase):
    def setUp(self):
        self.app = bottle.Bottle(catchall=False)

    def test_with_keyword(self):
        self.plugin = self.app.install(Plugin())

        @self.app.get('/')
        def test(queue):
            self.assertEqual(type(queue), type(hotqueue.HotQueue("queue")))
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

    def test_with_keyword_and_config(self):
        self.plugin = self.app.install(Plugin())

        @self.app.get('/', queue={'queue': 'myqueue'})
        def test(myqueue):
            self.assertEqual(type(myqueue), type(hotqueue.HotQueue("myhotqueue")))
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)


    def test_without_keyword(self):
        self.plugin = self.app.install(Plugin())

        @self.app.get('/')
        def test():
            pass
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

        @self.app.get('/2')
        def test(**kw):
            self.assertFalse('queue' in kw)
        self.app({'PATH_INFO':'/2', 'REQUEST_METHOD':'GET'}, lambda x, y: None)
        
if __name__ == '__main__':
    unittest.main()
