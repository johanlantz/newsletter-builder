import os
import urllib2
import re


def write_generic_tag(tag, line):
  try:
  	res = re.search('<' + tag + '>(.*?)</'+ tag + '>', line)
  	tagContent = res.group(1)
  except AttributeError:
    print "Error: tag " + tag + " not found"
    quit()
  file = open("elements/" + tag + ".html", 'r') 
  templateContent = file.read()
  templateContent = templateContent.replace("***tag***", tagContent)
  out_file.write(templateContent)

def write_three_columns(start_line):
  
  localThreeColumns = three_columns
  for i in range(0, 3):
  	link = in_file.readline()
  	try:
  	  res = re.search('<link>(.*?)</link>', link)
  	  prodLink = res.group(1)
  	except AttributeError:
  	  print "Error: link tag not found inside three_columns"
  	  quit()

  	#Get the product info
  	response = urllib2.urlopen(prodLink)
  	html = response.read()

  	try:
  	  res = re.search("<h1 itemprop=\"name\">(.*?)</h1>", html)
  	  prodName = res.group(1)
  	  print prodName
  	except AttributeError:
  	  print "Error: Product name not found"
  	  quit()

  	try:
  	  res = re.search("<span itemprop=\"image\" content=\"(.*?)\"></span>", html)
  	  prodImageLink = res.group(1)
  	  print prodImageLink
  	except AttributeError:
  	  print "Error: Product image not found"
  	  quit()

  	try:
  	  res = re.search("<span id=\"our_price_display\" itemprop=\"price\">(.*?)</span>", html)
  	  prodPrice = res.group(1)
  	  print prodPrice
  	except AttributeError:
  	  print "Error: Product price not found"
  	  quit()

  	#Insert product info
  	
  	stringToReplace = "***link" + str(i + 1) + "***"
  	localThreeColumns = localThreeColumns.replace(stringToReplace, prodLink)

  	stringToReplace = "***image" + str(i + 1) + "***"
  	localThreeColumns = localThreeColumns.replace(stringToReplace, prodImageLink)

  	stringToReplace = "***name" + str(i + 1) + "***"
  	localThreeColumns = localThreeColumns.replace(stringToReplace, prodName)

  	stringToReplace = "***price" + str(i + 1) + "***"
  	localThreeColumns = localThreeColumns.replace(stringToReplace, prodPrice)


  #write the modified three_columns to file
  out_file.write(localThreeColumns)
  #skip closing three_columns
  in_file.readline()

#Read the html elements
in_file = open('elements/head_and_css.html', 'r')
head_and_css = in_file.read()

in_file = open('elements/preheader.html', 'r')
preheader = in_file.read()

in_file = open('elements/header.html', 'r')
header = in_file.read()

in_file = open('elements/h1.html', 'r')
h1 = in_file.read()

in_file = open('elements/img_big.html', 'r')
img_big = in_file.read()

in_file = open('elements/img_small.html', 'r')
img_small = in_file.read()

in_file = open('elements/three_columns.html', 'r')
three_columns = in_file.read()

in_file = open('elements/h3.html', 'r')
h3 = in_file.read()

in_file = open('elements/border.html', 'r')
border = in_file.read()

in_file = open('elements/spacer.html', 'r')
spacer = in_file.read()

in_file = open('elements/footer.html', 'r')
footer = in_file.read()

in_file = open('elements/closing_tags.html', 'r')
closing_tags = in_file.read()

#Create output file
try:
  os.remove("result_template.html");
except OSError:
  pass
  
out_file = open('result_template.html', 'w')

#Static parts of template
out_file.write(head_and_css)
out_file.write(preheader)
out_file.write(header)

in_file = open('newsletter.html', 'r')

line = in_file.readline()

while line != "":
  if line.find("h1") != -1:
    write_generic_tag("h1", line)
  elif line.find("img_big") != -1:
    out_file.write(img_big)
  elif line.find("img_small") != -1:
    out_file.write(img_small)
  elif line.find("<three_columns>") != -1:
  	write_three_columns(line)
  elif line.find("h3") != -1:
    write_generic_tag("h3", line)
  elif line.find("border") != -1:
    out_file.write(border)
  elif line.find("spacer") != -1:
    out_file.write(spacer)
  else:
  	if line.find("link") != -1:
  	  print "Unknown tag" + line

  line = in_file.readline()

#static end part
out_file.write(footer)
out_file.write(closing_tags)
