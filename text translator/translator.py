
from translate import Translator

translator = Translator(to_lang="ko")

try:
	with open('./test.txt','r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)

		with open('./test-korean.txt',mode='w') as my_file2:
			my_file2.write(translation)

except FileNotFoundError as e:
	print("check your file path silly :)")

