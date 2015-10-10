import pandas as pd
import codecs

df = pd.read_csv('unicodeProduct.csv', encoding = 'utf-8')

small_df = df[['Brand', 'Title', 'Colors']]

small_df.to_csv('ToSearchOnAmazon.csv', index = False)

fi = codecs.open('ToSearchOnAmazon.txt', 'rU', 'utf-8')
fo = open('AmazonString.txt','w')


for line in fi:
	string = str(line)
	new_string = string.replace(',',' ')
	newer_string = new_string.replace(' ','+')
	print newer_string
	fo.write(newer_string + "\n")
