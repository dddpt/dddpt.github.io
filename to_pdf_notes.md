

# printing to pdf:

wkhtmltopdf does an acceptable job:
wkhtmltopdf path/to/index.html CV_wkhtmltopdf.pdf

printing takes the layout for xs screens, but having 2 projects card per row on real xs screens sucks...

## todo for wkhtmltopdf conversion:

1) move projects section at end of CV
2) add col-xs-X class to col-6 project cards and col-2 col-9 header
3) add some `style="margin-bottom:400px"` to fix page breaks
4) wkhtmltopdf index.html CV_wkhtmltopdf.pdf

online-convert

## ILovePDF 2023

https://www.ilovepdf.com/html-to-pdf
- "tablet view"
- not "one long page"
- margin "big"