#!/bin/bash

# Make all tables responsive
# sed -i 's/<table>/<div class="table-responsive"><table>/g' *.html
# sed -i 's/<\/table>/<\/table><\/div>/g' *.html


for file in *.html; do
  echo '<style>Add custom CSS HERE be carefull with identation.</style>' >> "$file"
done
