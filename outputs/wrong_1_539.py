def search ( var__0 , var__1 ) : 
  try:
    sDx=iter(range ( len ( var__1 ) ))
    while True:
      var__2=next(sDx)
      
      if var__1 [ var__2 ] >= var__0 : 
        break 
      elif var__1 [ - 1 ] < var__0 : 
        return len ( var__1 ) 
  except StopIteration:
    pass
  return var__2 

