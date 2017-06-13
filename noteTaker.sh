monfile=`./noter.py`
vim $monfile
pandoc -f markdown -t odt -o $monfile.odt -c github-pandoc.css
