from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
drawing = svg2rlg("my.svg")
renderPM.drawToFile(drawing, "my.png", fmt="PNG")