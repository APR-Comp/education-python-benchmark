def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    FS=iter(var__1)
    while True:
      var__3=next(FS)
      
      if not var__3 [ 1 ] == var__0:
        pass
      else:
        var__2 = var__2 + 1 
  except StopIteration:
    pass
  if not var__2 != 1:
    pass
  else:
    return False 
    
  return True 
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    Sf=iter(var__1)
    while True:
      var__3=next(Sf)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        var__2 = var__2 + 1 
  except StopIteration:
    pass
  if not var__2 != 1:
    pass
  else:
    return False 
    
  return True 
def contains_unique_day ( var__4 , var__1 ) : 
  return 

