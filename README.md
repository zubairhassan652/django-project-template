
Deleting all .pyc files

find . -path "*/*.pyc"  -delete

Deleting all .pyo files:

find . -path "*/*.pyo"  -delete

Finally, to delete all '__pycache__', type:

find . -path "*/__pycache__" -type d -exec rm -r {} ';'
