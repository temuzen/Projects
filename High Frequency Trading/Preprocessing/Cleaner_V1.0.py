import re
uncleanText = open("Nifty50data.txt").read()
cleanText = re.sub('[^A-Za-z0-9\s\n:\'/.]+', '', uncleanText)
open('words.txt', 'w').write(cleanText)


