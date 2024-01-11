def search ( var__0 , var__1 ) : 
  try:
    PA=iter(var__1)
    while True:
      var__2=next(PA)
      
      if  var__0 <= var__2:
          pass
      else:
        break 
      var__3 += 2 
  except StopIteration:
    pass
  return var__3 

