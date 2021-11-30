x,y,z = map(float, input().split())

if x < y+z and y < x+z and z < x+y:
    perimeter = round(x+y+z,1)
    print("Perimetro = {}".format(perimeter))
else:
    area = ((x+y)/2)*z
    area = round(area,1)
    print("Area = {}".format(area))