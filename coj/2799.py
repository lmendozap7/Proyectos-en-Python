angulo1 = int(raw_input())
angulo2 = int(raw_input())
angulo3 = int(raw_input())
if angulo1 + angulo2 + angulo3 != 180:
    print 'Error'
else:
    if angulo1 == angulo2 == angulo3:
        print 'Equilateral'
    elif angulo1 == angulo2 or angulo2 == angulo3 or angulo1 == angulo3:
        print 'Isosceles'
    else:
        print 'Scalene'
