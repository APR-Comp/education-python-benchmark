def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    AYYP=iter(var__1)
    while True:
      var__3=next(AYYP)
      
      if not var__3 [ 0 ] == var__0:
        pass
      else:        
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 <= 1 
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    mi=iter(var__1)
    while True:
      var__3=next(mi)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:  
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 <= 1
 
def contains_unique_day ( var__4 , var__1 ) : 
  var__5 = ( ) 
  try:
    OkE=iter(var__1)
    while True:
      var__3=next(OkE)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:      
        var__5 += ( var__3 , ) 
  except StopIteration:
    pass
  try:
    JFlBchX=iter(var__5)
    while True:
      var__3=next(JFlBchX)
      
      if not unique_day ( var__3 [ 1 ] , var__1 ):
        pass
      else:  
       return True 
  except StopIteration:
    pass
  return False 

