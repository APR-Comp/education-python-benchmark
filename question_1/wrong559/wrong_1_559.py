def search ( var__0 , var__1 ) : 
  try:
    dzX=iter(enumerate ( var__1 ))
    while True:
      var__2 , var__3=next(dzX)
      if var__3 == var__0 : 
        var__4 = var__2 + 1 
      elif var__3 > var__0 : 
        var__4 = var__2 
  except StopIteration:
    pass
  return var__4 

