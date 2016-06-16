import sys, os
import re

END_SYMBOL = re.compile("\s*</text>\s*")

def create_toy_corpus(path_to_corpus):
	line_counter = 0
	with open(path_to_corpus, 'r') as fcorpus:
		with open("wiki_toy_corpus.words", 'w+') as ftoy:
			line = fcorpus.readline()
			line_counter += 1
			while (line != ""):
				ftoy.write(line)
				if END_SYMBOL.match(line):
					break
				line = fcorpus.readline()
				line_counter += 1
	
	print("%s lines were taken" % line_counter)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Usage")
	else:
		create_toy_corpus(sys.argv[1])
		