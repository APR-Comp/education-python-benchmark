def search ( var__0 , var__1 ) : 
  if not var__1 != ( ):
    pass
  else:
    return - 1 
    
  try:
    lPoGR=iter(enumerate ( var__1 ))
    while True:
      var__2 , var__3=next(lPoGR)
      if not var__0 <= var__3:
          pass
      else:
          return var__2 
  except StopIteration:
    pass
  return var__2 + 1 

