import os
from dataclasses import dataclass
from tkinter import Tk
from tkinter.filedialog import askdirectory

@dataclass
class FilePath:
    path: str
    name: str

if __name__ == '__main__':
    paths = {}
    
    Tk().withdraw()

    paths['root']    = askdirectory(title='Select folder')
    paths['project'] = os.path.join(paths['root'], 'webstart')
    paths['assets']  = os.path.join(paths['project'], 'assets')
    paths['script']  = os.path.join(paths['assets'],  'script')
    paths['style']   = os.path.join(paths['assets'],  'style')

    files = [
        FilePath(paths['project'], 'index.html'),
        FilePath(paths['script'],  'script.js'),
        FilePath(paths['style'],   'style.css'),
    ]

    for file in files:
        try:
            if not os.path.exists(file.path):
                os.makedirs(file.path)
            open(os.path.join(file.path, file.name), 'x').close()
        except OSError as e:
            print('Ooopss... %s' %e)
