import re, urllib.request
print("searching: http://www.soic.indiana.edu/about/contact/index.html")
searching = urllib.request.urlopen("http://www.soic.indiana.edu/about/contact/index.html")

contents = searching.read().decode(errors = "replace")

searching.close()
print("Found the following phone numbers: ")
formatted = re.findall('[(][\d]{3}[)] [\d]{3}-[\d]{4}',contents)
for i in formatted:
      print(i)
