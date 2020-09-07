

class Prompt():

	@staticmethod
	def prompt(msg, inputType = str, allowedSet=None):
	    #print(allowedSet,type(allowedSet)
		while (True):
			try:
				res = inputType(input(f"{msg} {allowedSet}"))
				if (allowedSet is not None and res not in allowedSet):
					raise Exception('Not in allowed Set')
				break
			except ValueError as e1:
				print(f"1:Some Error {e1}")
			except Exception as e2:
				print(f"2:Some Error {e2}")
			finally:
				pass

		return res
