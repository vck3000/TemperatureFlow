import png
p = [(0, 0,  0, 0, 0,  0, 0, 0,  0, 0, 0, 0),
     (255, 0,  0, 255, 0,  0, 255, 0,  0, 255, 0, 0),
     (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255),
     (255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255),
     (255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0),
     (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255),
     (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255),
     (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255),
     ]
f = open('2.png', 'wb')
w = png.Writer(4, 8, greyscale=False)
w.write(f, p)
f.close()
