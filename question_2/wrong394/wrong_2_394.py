def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    EV=iter(var__1)
    while True:
      var__3=next(EV)
      
      if not var__3 [ 1 ] == var__0:
        pass
      else:
        var__2 = var__2 + 1 
  except StopIteration:
    pass
  if not var__2 != 1:
    return True 
  else:
    return False 
    
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    EcMk=iter(var__1)
    while True:
      var__3=next(EcMk)
      
      if not var__3 [ 0 ] == var__4:
        pass
      else:
        var__2 = var__2 + 1 
  except StopIteration:
    pass
  if not var__2 != 1:
    return True 
  else:
    return False 
    
def contains_unique_day ( var__4 , var__1 ) : 
  var__5 = ( ) 
  try:
    QC=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(QC)
      
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__5 += ( var__1 [ var__6 ] , ) 
  except StopIteration:
    pass
  var__7 = "" 
  var__8 = 0 
  try:
    My=iter(range ( len ( var__5 ) ))
    while True:
      var__6=next(My)
      var__7 = var__5 [ var__6 ] [ 1 ] 
      if not unique_day ( var__7 , var__1 ) == True:
        pass
      else:  
        var__8 = var__8 + 1 
      if not var__8 == 0:
        return True 
      else:
        return False 
  except StopIteration:
    pass

