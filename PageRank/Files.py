import glob
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import shutil, os

flag = 0;
search = input("What do you want to search?\n")

for filepath in glob.iglob('Pages/Temp/*.html'):
	f = open(filepath, "r")
	for line in f:
		if fuzz.WRatio(search, line) > 76:
			shutil.copy(filepath, 'Pages/') 
			flag =1
			break
		else:
			flag = 0
	if flag ==0:
		print("Not in file")




