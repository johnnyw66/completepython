#import sys
#print(sys.path)
import unittest
import basetest
import cap

from unittest import skip as skip
from basetest import BaseUnitTest


class DummyClass1(BaseUnitTest):

	def test_1(self):

#		_fnc_name = sys._getframe(0).f_code.co_name  # Alternatively missing out the 0 - gives current frame
#		_line_number = sys._getframe(0).f_lineno
#		_filename = sys._getframe(  ).f_code.co_filename
		print(f"function: {BaseUnitTest.who_am_i()},Line: {BaseUnitTest.where_am_i()} File:{BaseUnitTest.which_file()}")
		print(f"Module:{__name__} Class:{type(self).__name__} Class:{self.__class__.__name__} ")
		self.assertTrue(True) 

	def test_2(self):
		print("Test2 " + type(self).__name__)
		self.assertEqual(cap.cap_text('python'), 'Python')


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
