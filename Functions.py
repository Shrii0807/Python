# A function in python is defined by def keyword
# Example Python Code for User-Defined function  
def square( num ):    
    """  
    This function computes the square of the number.  
    """    
    return num**2     
object_ = square(6)    
print( "The square of the given number is: ", object_ )  

#Passby reference and pass by value
# Example Python Code for Pass by Reference vs. Value  
# defining the function    
def square( item_list ):    
    '''''''This function will find the square of items in the list'''    
    squares = [ ]    
    for l in item_list:    
        squares.append( l**2 )    
    return squares    
    
# calling the defined function    
my_list = [17, 52, 8];    
my_result = square( my_list )    
print( "Squares of the list are: ", my_result )    

#lambda function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
