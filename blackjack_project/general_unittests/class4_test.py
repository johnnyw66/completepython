"""
"""
import unittest
from unittest import skip as skip

import cap


class DummyClass1(unittest.TestCase):

	def test_1(self):
		print("Test1 " + __name__)
		self.assertTrue(True) 

	def test_2(self):
		print("Test2 " + __name__)
		self.assertEqual(cap.cap_text('python'),'Python')


	def test_3(self):
		print("Test3 " + __name__)
		self.assertNotEqual(cap.cap_text('python'), 'xython')

	
	def test_4(self):
		#self.assertEqual(cap.cap_text('python'),'Python')
		print("Test4 " + __name__)
		self.assertEqual(cap.cap_text('python world', True), 'Python World')
#		self.assertTrue(True)

	@skip('@TODO after module xxx completed')
	def test_5(self):
		print("Test5 " + __name__)
		self.assertTrue(False) 


if (__name__ == '__main__'):
	unittest.main()

