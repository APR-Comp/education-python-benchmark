def unique_day ( var__0 , var__1 ) : 
  var__2 = 2 
  try:
    zxajHMq=iter(var__1)
    while True:
      var__3=next(zxajHMq)
      
      if not var__3 [ 1 ] == var__0:
        pass
      else:
        var__2 += 1 
  except StopIteration:
    pass
  if not var__2 == 1:
    pass
  else:
    return True 
  return False 
def unique_month ( var__4 , var__1 ) : 
  var__5 = 0 
  try:
    XIe=iter(var__1)
    while True:
      var__3=next(XIe)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        var__5 += 1 
  except StopIteration:
    pass
  if not var__5 == 1:
    pass
  else:
    return True 
    
  return False 
def contains_unique_day ( var__4 , var__1 ) : 
  var__6 = ( ) 
  try:
    lMcrfRt=iter(var__1)
    while True:
      var__3=next(lMcrfRt)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        var__6 += ( var__3 [ 1 ] , ) 
  except StopIteration:
    pass
  try:
    vunkfBO=iter(var__6)
    while True:
      var__3=next(vunkfBO)
      
      if not unique_day ( var__3 , var__1 ) == True:
        pass
      else:
        return True 
  except StopIteration:
    pass
  return False 

