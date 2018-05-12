##CHALLENGE #1: (20 points)
##The names for the FBI’s top ten most wanted. Use file ‘fbi.html’
##We don’t expect you to write the solution for the case where the HTML would update – just for the HTML provided.
##Hint: BS4 outputs a list. Use a for-loop to narrow your selection even more.
##Hint: You’ll need to look at the HTML in order to figure out what to grab to solve this challenge.
##Reference URL: https://www.fbi.gov/wanted/topten

file = open(‘fbi.html’, ‘r’, encoding=’utf-8’)
html = file.read()
file.close()

soup = BeautifulSoup(html, ‘html.parser’)
htags = soup.find_all(‘h3’)
for htag in hatgs;
	atag = htag.find(‘a’)
	print(atag.string)

 
##CHALLENGE #2: (20 points)
##Print the name and URL for all on-campus academic programs through SOIC.
##Use file ‘degrees.html’
##Reference URL: https://www.indiana.edu/academics/degrees-majors/index.html?school=School%20of%20Informatics%20and%20Computing&distance_ed=N

file2 = open(‘degrees.html’, ‘r’)
html2 = file2.read()
file2.close()
soup = BeautifulSoup(html2, ‘html.parser’)

links = soup.find_all(href=re.compile(‘degree/’))
print(‘Opportunities at Indiana University:’)
for item in links:
	print(item.string)
	print(item.get(“href”), ‘\n’)

 

##CHALLENGE #3: (20 points)
##Print all U.S. multi-state foodborne outbreak investigations for 2016 and 2017.
##Use file ‘outbreaks.html’
##Hint: find_all() returns a list with the results. You can’t call a second find_all() on the resulting list (.find_all takes a string), but could you do so on the items within the list?
##Reference URL: https://www.cdc.gov/foodsafety/outbreaks/multistate-outbreaks/outbreaks-list.html
 
file3 = open(‘outbreaks.html’, ‘r’)
html3 = file3.read()
file3.close()

soup = BeautifulSoup(html3, ‘html.parser’)
for name in soup.find_all(‘div’, id=[‘tabs-1’,’tabs-2’]):
	datab= name.find_all(‘a’)
	For item in data:
		print(item.get_text))
