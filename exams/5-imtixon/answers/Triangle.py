class Triangle(object):

    def __init__(self, a, b, c):
        self.ax = a[0]
        self.ay = a[1]
        
        self.bx = b[0]
        self.by = b[1]
        
        self.cx = c[0]
        self.cy = c[1]
        
    def area(self):
        ab = ( (self.ax - self.bx)**2 + (self.ay - self.by)**2 ) ** 0.5
        ac = ( (self.ax - self.cx)**2 + (self.ay - self.cy)**2 ) ** 0.5
        bc = ( (self.cx - self.bx)**2 + (self.cy - self.by)**2 ) ** 0.5
        
        # uchburchak bo'lolmasa
        if ab > ac + bc or ac > ab + bc or bc > ab + ac:
            return 0
        
        p = (ab + ac + bc) / 2
        area = (p * (p - ab) * (p - ac) * (p - bc)) ** 0.5

        return round(area,2)

a = []
ax = a.append(int(input()))
ay = a.append(int(input()))

b = []
bx = b.append(int(input()))
by = b.append(int(input()))

c = []
cx = c.append(int(input()))
cy = c.append(int(input()))

tri = Triangle(a, b, c)
print(tri.area())