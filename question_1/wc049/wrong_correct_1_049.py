def search ( var__0 , var__1 ) : 
  try:
    xaU=iter(range ( len ( var__1 ) ))
    while True:
      var__2=next(xaU)
      
      if  var__0 <= var__1 [ var__2 ]:
        pass
      else:
        return var__2 
  except StopIteration:
    pass
  return len ( var__1 ) 

