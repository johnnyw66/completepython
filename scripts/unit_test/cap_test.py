"""
"""
import unittest
import cap
from my_unit_tests.basetest import BaseUnitTest

class CapTest(BaseUnitTest):

	def test_one_word(self):
		print(BaseUnitTest.who_am_i())
		self.assertEqual(cap.cap_text('python'),'Python')

	def test_multi_words_default(self):
		print(BaseUnitTest.who_am_i())
		self.assertEqual(cap.cap_text('python rocks'),'Python rocks')

	def test_multi_words_false(self):
		print(BaseUnitTest.who_am_i())
		self.assertEqual(cap.cap_text('python rocks',False),'Python rocks')

	def test_multi_words(self):
		print(BaseUnitTest.who_am_i())
		self.assertEqual(cap.cap_text('python rocks',True),'Python Rocks')

	"""
			Other examples
	"""

	def test_isupper(self):
		print(BaseUnitTest.who_am_i())
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())


	def test_upper(self):
		print(BaseUnitTest.who_am_i())
		self.assertEqual('foo'.upper(), 'FOO')
	
	def test_split(self):
		print(BaseUnitTest.who_am_i())
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

class CapTest2(BaseUnitTest):
	
	def setUp(self):
		print(BaseUnitTest.who_am_i())

	def tearDown(self):
		print(BaseUnitTest.who_am_i())


	def test_one(self):
		print(BaseUnitTest.who_am_i())
		self.assertTrue(True)

	def test_two(self):
		print(BaseUnitTest.who_am_i())
		self.assertTrue(True)

	def test_three(self):
		print(BaseUnitTest.who_am_i())
		self.assertTrue(True)

	@unittest.skip("demonstrating skipping -v for this message to be seen")
	def test_four(self):
		print(BaseUnitTest.who_am_i())
		self.assertTrue(True)

class CapTest3(unittest.TestCase):


	def runTest(self):
		print("****RUN TEST CAPTEST3****")
		self.assertTrue(True)

	def test_1(self):
		print("****RUN TEST_1 CAPTEST3****")
		self.assertTrue(True)

	def test_2(self):
		print("****RUN TEST_2 CAPTEST3****")
		self.assertTrue(True)

def suite():
	tests = ['test_1', 'test_2']
	return unittest.TestSuite(map(CapTest3, tests))

if (__name__ == '__main__'):
	unittest.main()
	#alltests = unittest.TestSuite([suite()])
	pass

