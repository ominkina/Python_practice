#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    path = "/Users/Olga/Desktop/google-python-exercises/babynames"
    os.chdir(path)
    
    year = re.search(r'\d\d\d\d', filename)
    year = year.group()

    #open file, read in line by line
    f = open(filename, 'r')

    #pull out ranks and names, delete surrounding characters
    names = re.findall(r'<td>\w+</td>', f.read())
    for i in range(0, len(names)):
        names[i] = names[i].replace('<td>','')
        names[i] = names[i].replace('</td>','')

    #populate list
    list = [year]
    for i in range(0, len(names), 3):
        rank = names[i]
        string1 = '%s %s' %(names[i+1], rank)
        string2 = '%s %s' %(names[i+2], rank)
        list.append(string1)
        list.append(string2)

    print sorted(list)
    return
    
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  extract_names(args[0])
  
if __name__ == '__main__':
  main()
