def quadrature(f, a, b):
    
    mid = (a+b)/2
    size = b-a
    ecart = np.sqrt(3/20) * size  #A calculer une fois comme variable global
    
    p1 = f(mid - ecart)
    p2 = f(mid)
    p3 = f(mid + ecart)
    
    
    intval = (5*p1 + 8*p2 + 5*p3)*size/18
    
    return intval
