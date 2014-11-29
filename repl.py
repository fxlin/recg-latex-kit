#!/usr/bin/env python

'''
usage: repl.py mybib > /tmp/test.bib

https://developers.google.com/edu/python/regular-expressions
'''

import sys
import re

# each entry:
# [ "keywords in full booktitle as from the raw ACM bibtex entry", 
#   "short name as used in abr-{short|long}.bst"]
#

all_conf_list = [
	["USENIX Annual Technical Conference", "ATC"],
	["USENIX Conference on Annual Technical Conference", "ATC"],  # sometimes this might appear
	["International Conference on Mobile Systems, Applications, and Services", "MOBISYS"],
	["International Conference on Mobile Computing and Networking", "MOBICOM"],
	["International Joint Conference on Pervasive and Ubiquitous Computing", "UBICOMP"],
	["SIGPLAN Conference on Programming Language Design and Implementation", "PLDI"],
	["Conference on Operating Systems Design and Implementation", "OSDI"],
	["Symposium on Operating Systems Design and Implementation", "OSDI"], # old name?	
	["ACM Symposium on Operating Systems Principles", "SOSP"],
	["ACM SIGOPS Symposium on Operating Systems Principles", "SOSP"],	# also this...
	["International Symposium on Computer Architecture", "ISCA"],
	["Conference on Architectural Support for Programming Languages and Operating Systems", "ASPLOS"],
	["Conference on Networked Systems Design and Implementation", "NSDI"],
	["SIGCOMM Conference on Internet Measurement", "IMC"],
	["International Conference on World Wide Web", "WWW"],
	["Workshop on Mobile Computing Systems and Applications", "HOTMOBILE"],
]

def repl_confname(conf_list, line):
	ever_matched = False
	#if line[0] == "#":	# comment line
	if re.search("^\s*#.*", line):  # line begins with #
		print line,
		return
		
	# try to match against all conf names
	for fullname, shortname in conf_list:
		ex1=r'''(.*)(booktitle =)(.*''' + fullname + '''.*)'''
		match = re.search(ex1, line, re.IGNORECASE)
		if match:
			if ever_matched == True:	# this line matches multiple patterns, why???
				sys.stderr.write("error: line: " + line)
			else:
				print match.group(1) + "booktitle-full =" + match.group(3)
				print "%sbooktitle = %s," %(match.group(1), shortname)
				ever_matched = True			
	# no match in any conf
	if not ever_matched:
		print line,

if __name__ == "__main__":    
    f=file(sys.argv[1])
    lines = f.readlines()
    for line in lines:  
		repl_confname(all_conf_list, line)
