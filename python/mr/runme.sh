echo "this is a book, this is a pen" | python mapper.py | sort -k 1 | python reducer.py
