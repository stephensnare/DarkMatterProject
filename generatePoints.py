from classes.point import Point

def generate():
    numPoints = 10
    for i in range(numPoints):
        point = Point()
        print('point x: ', point.x)
        print('point y: ', point.y)
        print('point z: ', point.z)
        print('\\')


generate()