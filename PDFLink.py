import fitz
import sys
if (len(sys.argv) != 4):
  print("Usage: python "+sys.argv[0]+" source.pdf links_dump output.pdf")
else:
  doc = fitz.open(sys.argv[1])
  linksToAdd = 	open(sys.argv[2],"r").read().split("\n")
  for l in linksToAdd:
    if (l != ""):
      l = l.split("\t")
      doc.loadPage(int(l[2])).insertLink({"kind": 2, "from": fitz.Rect(*list(map(int,l[0].split(",")))), "uri": l[1]})
  doc.save(sys.argv[3])
  doc.close();
