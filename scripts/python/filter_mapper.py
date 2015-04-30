#!/usr/bin/python
import sys
import os

lines = open('tst.txt','r').readlines()
articles_list = [x.strip() for x in lines]

articles = dict(zip(articles_list, [1 for t in articles_list]))

#print'%s\t%s' % (str(articles), 1)

#path = os.getcwd()
#files = os.listdir(path)


#print'%s\t%s' % (path, 1)
#print'%s\t%s' % (str(lines[0]).strip(), 1)

#for f in files:
#  print'%s\t%s' % (f, 1)


wiki=str(os.environ["WIKI_PROJ"]).strip()

#print'%s\t%s' % (wiki, 1)


#for l in lines: 
#  print'%s\t%s' % (l[0], 1)


for line in sys.stdin:
  line = line.strip()
  #print '%s\t%s' % (line, 1)
  #print line
  #continue


  toks = line.split()
  try:
    id = toks[0]
    proj = toks[1]
    art = toks[2]
    if proj != wiki:
      continue
    if not art in articles:
      continue
    print line
  except IndexError:
    continue

#  for w in words:
#    print '%s\t%s' % (w, 1)
  
