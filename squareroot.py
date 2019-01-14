import cs50

print("welcome to square root algorithm")

# starting with input to which we are going to find square root
#
def squareRoot(x):
    x = float(x)
    # assume a number g (guess no.) as a square root of x
    g = x/100
    
    # To find square root we have write a loop
    
    if g*g == x :
        return round(g, 8)
    else:
        while round(g*g, 4) != float(x):
            g=(g+(x/g))/2
            g= round(g, 8)
        return round(g, 4)

