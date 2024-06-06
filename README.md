# Watermark

## Add watermarks to your pdf files

Download this git repository to get the code on your machine :
```bash
git clone https://github.com/MathieuHmmt/watermark.git
```

Install the necessary python packages (pypdf and reportlab)

``` bash
pip3 install pypdf reportlab
```

Or you can use the `requirements.txt` file :

``` bash
pip3 install -r requirements.txt
```

Create a `docs` folder and put your PDF files into it.
Then you can launch the script with

``` bash
 python3 add_watermark.py <watermark_text>
```

and you will get your watermarked PDFs in the `watermarked` folder.

> You can adjust the opacity and the angle of the watermark text with optional parameters.

Example :
`python3 add_watermark.py "Confidential" --opacity=0.15 --angle=25`

> Tips : Use imagemagick to convert or combine images into a pdf with `convert img1 img2 output.pdf`
