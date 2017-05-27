
import sys, xdrlib 
import xlrd
from pprint import pprint
from array import array
 

def open_excel(file = 'execlFile.name'):
	try:
		data = xlrd.open_workbook(file)
		pprint(data, indent=3)
		return data
	except FileNotFoundError:
		print(str("error")) 


data = open_excel("test.xlsx")		

def dump(obj):
  for attr in dir(obj):
    print ("obj.%s = %s" % (attr, getattr(obj, attr)))

 

sheet = data.sheets()[0]
nRows = sheet.nrows
nCols = sheet.ncols
for i in range(1, nRows) :

	print(sheet.row_values(i))


a=[]
a.append(3)
a.append(4)
a.append(1)

for item in a:
	print(item)

print(a)