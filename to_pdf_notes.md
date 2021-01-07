

# printing to pdf:

wkhtmltopdf does an acceptable job:
wkhtmltopdf path/to/index.html CV_wkhtmltopdf.pdf

printing takes the layout for xs screens, but having 2 projects card per row on real xs screens sucks...

## todo for wkhtmltopdf conversion:

1) move projects section at end of CV
2) add col-xs-X class to col-6 project cards and col-2 col-9 header
3) add some _style="margin-bottom:400px"_ to fix page breaks
4) wkhtmltopdf index.html CV_wkhtmltopdf.pdf