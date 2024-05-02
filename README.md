# Watermark

## Add watermarks to your pdf files

Just create a `docs` folder and put your PDF files into it.
Then you can launch the script with `./add_watermark <watermark_text>` and you will get your watermarked PDFs in the `watermarked` folder.
You can adjust the opacity and the angle of the watermark text with optional parameters.

Example :
`./add_watermark "Confidential" --opacity=0.15 --angle=25`

> Tips : Use imagemagick to convert or combine images into a pdf with `convert img1 img2 output.pdf`