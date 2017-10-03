import shutil
import os



src = 'C:\Users\Daler Rakhmet-Zade\Desktop\The Tech Academy\Python\Python Drills\shutil drill\Folder A' #'source'
dst = 'C:\Users\Daler Rakhmet-Zade\Desktop\The Tech Academy\Python\Python Drills\shutil drill\Folder B' #'destination'

files = os.listdir(src)
    
for file in files:
    src_file = os.path.join(src, file)
    dst_file = os.path.join(dst, file)
    shutil.move(src_file, dst_file)
    print(src_file, dst_file)
    
