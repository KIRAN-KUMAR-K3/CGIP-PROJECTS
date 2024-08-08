from vpython import canvas, box, cylinder, vector, color, rate

scene = canvas(width=800, height=600, background=color.white)

def draw_cuboid(pos, length, width, height, color):
    cuboid = box(pos=vector(*pos),
                 length=length,
                 width=width,
                 height=height,
                 color=color)
    return cuboid

def draw_cylinder(pos, radius, height, color):
    cyl = cylinder(pos=vector(*pos),
                   radius=radius,
                   height=height,
                   color=color)
    return cyl

def translate(obj, dx, dy, dz):
    obj.pos += vector(dx, dy, dz)

def rotate(obj, angle, axis):
    obj.rotate(angle=angle, axis=vector(*axis))


def scale(obj, sx, sy, sz):
    obj.size = vector(obj.size.x * sx, obj.size.y * sy, obj.size.z * sz)


cuboid = draw_cuboid((-2, 0, 0), 2, 2, 2, color.blue)

translate(cuboid, 4, 0, 0)

rotate(cuboid, angle=45, axis=(0, 1, 0))

scale(cuboid, 1.5, 1.5, 1.5)

cylinder = draw_cylinder((2, 2, 0), 1, 10, color.red)

translate(cylinder, 0, -2, 0)

rotate(cylinder, angle=30, axis=(1, 0, 0))

scale(cylinder, 1.5, 1.5, 1.5)

while True:
    rate(30)
