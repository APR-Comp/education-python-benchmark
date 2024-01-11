def unique_day ( var__0 , var__1 ) : 
  var__2 = ( ) 
  try:
    BGezv=iter(var__1)
    while True:
      var__3=next(BGezv)
      var__2 += ( var__3 [ 0 ] , ) 
  except StopIteration:
    pass
  var__4 = 0 
  try:
    EWIvuObQGxe=iter(var__2)
    while True:
      var__5=next(EWIvuObQGxe)
      
      if not var__0 == var__5:
        pass
      else:
        var__4 += 1 
  except StopIteration:
    pass
  if not var__4 != 1:
    pass
  else:
    return False 
    
  return True 
def unique_month ( var__6 , var__1 ) : 
  var__7 = ( ) 
  try:
    mvy=iter(var__1)
    while True:
      var__3=next(mvy)
      var__7 += ( var__3 [ 0 ] , ) 
  except StopIteration:
    pass
  var__4 = 0 
  try:
    mp=iter(var__7)
    while True:
      var__5=next(mp)
      if not var__6 == var__5:
        pass
      else:
        var__4 += 1 
  except StopIteration:
    pass
  if not var__4 != 1:
    pass
  else:
    return False 
    
  return True 
def contains_unique_day ( var__6 , var__1 ) : 
  var__5 = ( ) 
  try:
    OkTGsCkp=iter(var__1)
    while True:
      var__3=next(OkTGsCkp)
      
      if not unique_day ( var__3 [ 1 ] , var__1 ):
        pass
      else:
        var__5 += ( var__3 [ 0 ] , ) 
  except StopIteration:
    pass
  try:
    xet=iter(var__5)
    while True:
      var__2=next(xet)
      if not var__6 in var__5:
        pass
      else:
        return True 
      break 
    
  except StopIteration:
    pass
  return False 

