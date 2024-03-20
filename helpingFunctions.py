def euclidGCD(x,y): # from Lecture 4 Slide 13 
    if y == 0:
        return x
    else:   
        return euclidGCD(y, x%y)

