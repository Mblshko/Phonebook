from os.path import exists
from file_menegement import File
from interface import Interface


path = "telephone_book.csv"
valid = exists(path)
if not valid:
    File.file_create()

Interface.start()
