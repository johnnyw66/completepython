import unittest
import sys


class BaseUnitTest(unittest.TestCase):
	@staticmethod
	def who_am_i():
		# frame '1' is the 'calling frame'
		return sys._getframe(1).f_code.co_name

	@staticmethod
	def where_am_i():
		return sys._getframe(1).f_lineno

	@staticmethod
	def which_file():
		return sys._getframe(1).f_code.co_filename
