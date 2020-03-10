javascript:
(width => {
  const mmToPDF = (mm => mm*72/25.4);
  let bodyOffset = document.querySelector("body").getBoundingClientRect();
  const pxToPDF = ((body) => {
    return (px => mmToPDF(px*width/body.width));
  })(bodyOffset);
  bodyOffset = [parseFloat(bodyOffset.x),parseFloat(bodyOffset.y)];
  let links = [...document.querySelectorAll("a")].map(e => {
    let href = e.href;
    e = e.getBoundingClientRect();
    let values = [e.x,e.y,e.width,e.height].map(e => parseFloat(e));
    values[2] = values[0]+values[2];
    values[3] = values[1]+values[3];
    values = values.map((e,i) => {
      return Math.round(pxToPDF(e-bodyOffset[i%2]))
    });
    return values.join(",")+"\t"+href
  });
  alert(links.join("\n"));
})(parseInt(prompt("Width ? (mm)")))
