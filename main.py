from stats import wordcount

def get_book_text(path_to_file):
	# do something with f (the file) here
	with open(path_to_file) as f:
		# f is a file object
		file_contents = f.read()
	#print(file_contents)
	return file_contents

def main():
	path_to_file = "./books/frankenstein.txt"
	text = get_book_text(path_to_file)
	words = wordcount(text)
	print(f"Found {len(words)} total words")

main()
