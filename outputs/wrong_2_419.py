def unique_day ( var__0 , var__1 ) : 
  var__2 = -1 
  try:
    fk=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(fk)  
      if not var__0 == var__1 [ var__3 ] [ 1 ]:
        var__2 = var__2 
      else:
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 == 1 
def unique_month ( var__4 , var__1 ) : 
  var__2 = 0 
  try:
    vLopKro=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(vLopKro)
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        var__2 = var__2 
      else:        
        var__2 += 1 
  except StopIteration:
    pass
  return var__2 == 1 
def contains_unique_day ( var__4 , var__1 ) : 
  return 

