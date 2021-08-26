# !/usr/bin/python

import mammoth
import glob, os

folder = os.getcwd()

#folder = "/home/example/DocxFiles"
# Specify the directory where the .docx files are located.
# Or leave as is and place all .docx files in the same directory as this script.

os.chdir(folder)

# Ignore images.
def ignore_image(image):
    return []

for file in glob.glob("*.docx"):
 with open(file, "rb") as docx_file:
  result = mammoth.convert_to_html(docx_file, convert_image=ignore_image)
  with open(file+".html", "w") as html_file:
   html_file.write(result.value)

   # Rename converted file to remove .docx extention
   os.system("rename 's/\.docx\.html$/.html/' *.docx.html")
