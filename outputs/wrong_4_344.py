def sort_age ( var__0 ) : 
  var__1 = 0 
  var__2 = ( ) 
  try:
    eYv=iter(var__0)
    while True:
      var__3=next(eYv)
      if  var__3 [ 1 ] > var__1:
        tuple ( var__3 ) + var__2 
      else:
        var__2 += tuple ( var__3 ) 
        var__1 = var__3 [ 1 ] 
  except StopIteration:
    pass
  return var__2 

