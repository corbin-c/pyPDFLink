# pyPDFLink

Python utility to add links to a PDF. Just a small script using [PyMuPDF]()https://pymupdf.readthedocs.io/).

## Installation

```
git clone git@https://github.com/corbin-c/pyPDFLink.git
cd pyPDFLink
pip install pymupdf
```

## Usage

`python PDFLink.py input_file.pdf links_dump output_file.pdf`

## Links description

Only hyperlinks are supported. Links must be described in a text file,
structured as TSV: First column is the "clickable box" rectangle definition,
as `x0,y0,x1,y1`, second column is the destination URI.

### Example:

```
27,293,104,307	tel:+43245676432
27,312,160,327	mailto:first.last@gmail.com
216,573,326,587	https://coolwebsite.com/
```

## Why this tool?

When using Firefox to generate a PDF from a web page, it comes without
hyperlinks. This tool can be used to add the links where they should be. To
avoid manually describing the box & uri for each hyperlink to activate, a
JS bookmarklet is provided (see file `bkmlt.js`).
