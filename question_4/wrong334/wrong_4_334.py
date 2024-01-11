def sort_age ( var__0 ) : 
  try:
    urxp=iter(range ( 1 , len ( var__0 ) ))
    while True:
      var__1=next(urxp)
      
      while var__0 [ var__1 ] [ 2 ] < var__0 [ var__1 - 1 ] [ 1 ] : 
        var__0 . pop ( var__1 ) 
        var__0 . insert ( var__1 - 1 , var__0 [ var__1 ] )       
  except StopIteration:
    pass
  return var__0 . reverse ( ) 

