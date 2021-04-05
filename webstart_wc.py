import os
from dataclasses import dataclass
from tkinter import Tk
from tkinter.filedialog import askdirectory

@dataclass
class FilePath:
    path:    str
    name:    str
    content: str

if __name__ == '__main__':
    paths = {}
    
    Tk().withdraw()

    paths['root']    = askdirectory(title='Select folder')
    paths['project'] = os.path.join(paths['root'],    'webstart')
    paths['assets']  = os.path.join(paths['project'], 'assets')
    paths['js']      = os.path.join(paths['assets'],  'js')
    paths['css']     = os.path.join(paths['assets'],  'css')

    # HARDCODE BEGIN - I JUST WANTED TO MAKE IT IN ONE FILE)
    content = {
        #index.html
        'index' : 
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebStart</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    
    <script src="assets/js/script.js"></script>
</body>
</html>
""",

        #style.css
        'style': 
"""* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}     
""",

        #script.js
        'script' : "'use strict'",
    }
# HARDCODE END - I JUST WANTED TO MAKE IT IN ONE FILE)


    files = [
        FilePath(
            paths['project'], 
            'index.html',
            content['index'],
        ),

        FilePath(
            paths['js'], 
            'script.js',
            content['script'],
        ),

        FilePath(
            paths['css'],
            'style.css',
            content['style'],    
        ),
    ]

    for file in files:
        try:
            if not os.path.exists(file.path):
                os.makedirs(file.path)
            with open(os.path.join(file.path, file.name), 'w') as fout:
                fout.write(file.content)
        except OSError as e:
            print('Ooopss... %s' %e)
