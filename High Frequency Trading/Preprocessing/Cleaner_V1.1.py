
import re

def Cleaner(File):
    uncleanText = open(str(File)+'.txt').read()
    cleanText = re.sub('[^A-Za-z0-9\s\n:\'/.,]+', '', uncleanText)#Direct Cleaning is possible..

    index = open('ind'+str(File)+'.txt').read()
    cleanindex = re.sub('[^A-Za-z0-9\s\n:\'/.,]+', '', index)
    open('Cleaned'+str(File)+'.csv', 'w').write(cleanindex)
    open('Cleaned'+str(File)+'.csv', 'a').write(cleanText)


'''
import pandas as pd
data =pd.read_csv('Optionsoctobercleaned.txt',sep=",")
DF = pd.DataFrame(data)
print(DF.columns[0:13])

'''