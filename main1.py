import os
import getpass
from MergeVideo import MergeAdder
from YoutubeAPICommands import YoutubeAPICommands

checkuser = getpass.getuser()
files = os.listdir(r"C:\\Users\\" + checkuser + '\\Documents\\VCC\\Today\'s Clips')

filex = files[:]
count = 0
for file in filex:
    if 'Final.mp4' in file:
        files[count] = files[count][:-9]
        count+=1
    else:
        files.pop(count)
mergeAdd = MergeAdder(files)
mergeAdd.merger()
