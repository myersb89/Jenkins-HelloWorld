import unittest
from hello import *

class MyFirstTests(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello_world(),"hello world")
