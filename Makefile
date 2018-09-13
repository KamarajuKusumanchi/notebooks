# taking the easy way for now. Afterwards, see
# https://github.com/jeremiedecock/pywi-cta-notebooks/blob/master/Makefile and
# generalize this accordingly.

html:
	jupyter nbconvert pandas/"Select rows and columns.ipynb" --to html --output-dir=html/pandas

clean:
	rm -rf html
