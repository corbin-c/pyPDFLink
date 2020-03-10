import fitz
print(fitz.__doc__)
doc = fitz.open("./resume.pdf")
links = doc.loadPage(0).getLinks()
print(links)
doc.loadPage(0).insertLink({'kind': 2, 'from': fitz.Rect(6.0, 350.0, 184.0, 366.0), 'uri': 'https://some-great-uri'})
doc.save("out.pdf")
doc.close();
