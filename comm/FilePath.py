import os
def path_file(file='apis',filename='add.xls',):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),file,filename)

