def search ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    We=iter(enumerate ( var__1 ))
    while True:
      var__3 , var__4=next(We)
      if not var__0 >= var__4:
        var__2 = var__3 + 1 
      else:
        var__2 = var__3 
        return var__2 
  except StopIteration:
    pass
  return var__2 

