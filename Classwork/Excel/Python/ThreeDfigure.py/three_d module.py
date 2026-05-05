import math
def cube_volume(a):
    return a**3
def cube_surface_area(a):
    return 6 *(a**2)
def cuboid_volume(l,b,h):
    return l*b*h
def cuboid_surface_area(l,b,h):
    return 2*(l*b+b*h+l*h)
def cuboid_curved_surface_area(l,b,h):
    return 2*h*(l+b)
def cyclinder_volume(r,h):
    return 2 *math.pi*r**2*h
def cyclinder_surface_area(r,h):
    return 2*math.pi*r*(r+h)
def cyclinder_curved_surface_area(r,h):
    return 2*math.pi*r*h
def cone_volume(r,h):
    return (1/3)*math.pi*r**2*h
def cone_surface_area(r,h):
    l= math.sqrt(r**2+h**2)
    return math.pi*r*(r+1)
def cone_curved_surface_area(r,h):
    l=math.sqrt(r**2+h**2)
    return math.pi*r*1
def sphere_volume(r):
    return(4/3)*math.pi*r**3
def sphere_surface_area(r):
    return 4 *math.pi*r**2
def hemisphere_volume(r):
    return(2/3)*math.pi*r**3
def hemisphere_surface_area(r):
    return 3*math.pi*r**2
def hemisphere_curved_surface_area(r):
    return 2 *math.pi*r**2


    

    



    
