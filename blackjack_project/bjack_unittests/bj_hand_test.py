#import sys
#print(sys.path)
import unittest
import basetest

from unittest import skip as skip
from basetest import BaseUnitTest

from packages.blackjack.hand import Hand
from packages.blackjack.card import Card



class Hand_UTest(BaseUnitTest):

	def addCards(self,hand):
		print("********ADD CARDS**********")

	def test_hand_create(self):

		print(f"function: {BaseUnitTest.who_am_i()},Line: {BaseUnitTest.where_am_i()} File:{BaseUnitTest.which_file()}")
		print(f"Module:{__name__} Class:{type(self).__name__} Class:{self.__class__.__name__} ")
		hand = Hand()
		self.assertEqual(hand.name,Hand.DEFAULT_HAND_NAME)
		self.assertEqual(len(hand.cards),0)
		card_hand = [1,2,3,4]
		hand.add([1,2,3,4])
		self.assertNotEqual(len(hand.cards),0)
		self.assertEqual(len(hand.cards),len(card_hand))
		hand.empty_hand()
		self.assertEqual(len(hand.cards),0)


	def test_hand_calcscore(self):
		print("Test2 " + type(self).__name__)
		hand = Hand('Johnny')
		self.assertEqual(hand.name,'Johnny')


	def test_3(self):
		print("Test3 " + __name__)
		hand = Hand()
		hand.add(1)
		hand.add(2)
		hand.add([3, 4, 5])
		hand.add(6)
		self.assertEqual(hash(str(hand.cards)), hash(str([1, 2, 3, 4, 5, 6])))



	def test_4(self):
		#self.assertEqual(cap.cap_text('python'),'Python')
		print("Test4 " + __name__)
		card = Card(0)
		print(card)	

		self.assertTrue(True)

	@skip('@TODO after module xxx completed')
	def test_5(self):
		print("Test5 " + __name__)
		self.assertTrue(False)


if (__name__ == '__main__'):
	unittest.main()
