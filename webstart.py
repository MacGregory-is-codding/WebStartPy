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
    paths['project'] = os.path.join(paths['root'],    'webstart')
    paths['assets']  = os.path.join(paths['project'], 'assets')
    paths['js']      = os.path.join(paths['assets'],  'js')
    paths['css']     = os.path.join(paths['assets'],  'css')

    files = [
        FilePath(paths['project'], 'index.html'),
        FilePath(paths['js'],      'script.js'),
        FilePath(paths['css'],     'style.css'),
    ]

    for file in files:
        try:
            if not os.path.exists(file.path):
                os.makedirs(file.path)
            open(os.path.join(file.path, file.name), 'w').close()
        except OSError as e:
            print('Ooopss... %s' %e)
