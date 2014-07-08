all: README.html

%.html:%.tex
	htlatex $^
