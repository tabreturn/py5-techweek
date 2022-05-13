# dimensions of the display window measured in pixels
size(800, 500)
background('#047')

# set outline
stroke('#FFFFFF')
stroke_weight(3)

# large red rectangle
fill('#F00')
rect(100, 150, 200, 300)

# small red rectangle
rect(10, 15, 20, 30)

# orange square
fill('#F90')
rect(50, 100, 150, 150)

# fill-less square
no_fill()
square(250, 100, 150)

# reposition coordinate system
translate(width/2, 0)

# points
point(100, 25)
point(200, 25)
point(150, 75)

# triangle
triangle(100, 25, 200, 25, 150, 75)

# ellipse
ellipse(100, 100, 100, 50)

# circle
circle(100, 100, 50)

# quad
quad(260, 180, 360, 200, 380, 250, 260, 280)

# line
y = 400  # variable
line(50, y, 50+200, y)
