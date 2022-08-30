path = "Images"


import os
from pydoc import classname
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames]


def convert(path: str):
    className = path[path.rfind("\\")+1:].replace(".png","")
    imgPath = "https://raw.githubusercontent.com/Digital-Dance-TrakLab/Traklab-Documentation/master/" + path.replace("\\","/")   
    markdownImg = "<img src=\"" + imgPath + "\" />"
    return (className, markdownImg)
    


res = map(convert, result)

import csv

# open the file in the write mode
f = open('class_table.csv', 'w')

# create the csv writer
writer = csv.writer(f)
writer.writerow(("Class", "Diagram"))


for r in res:
    writer.writerow(r)

# close the file
f.close()

print(*res)