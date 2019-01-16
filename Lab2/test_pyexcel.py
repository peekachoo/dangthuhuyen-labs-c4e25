import pyexcel
# make sure you had pyexcel-xls installed
from collections import OrderedDict

a_list_of_dictionaries = [
    OrderedDict({
        "Name": 'Adam',
        "Age": 28
    }),
    OrderedDict({
        "Name": 'Beatrice',
        "Age": 29
    }),
    OrderedDict({
        "Name": 'Ceri',
        "Age": 30
    }),
    OrderedDict({
        "Name": 'Dean',
        "Age": 26
    })
]
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")