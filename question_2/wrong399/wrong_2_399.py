def unique_day ( var__0 , var__1 ) : 
  var__2 = 0 
  try:
    DZUwSY=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(DZUwSY)
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
    me=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(me)
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        var__2 = var__2
      else:
        var__2 += 1
  except StopIteration:
    pass
  return var__2 == 1 
def contains_unique_day ( var__4 , var__1 ) : 
  var__5 = ( ) 
  var__6 = ( ) 
  try:
    Xp=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(Xp)
      if not var__4 == var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__5 = var__5 + ( ( var__1 [ var__3 ] [ 0 ] , var__1 [ var__3 ] [ 1 ] ) , )
  except StopIteration:
    pass
  try:
    ymJoIVlh=iter(range ( len ( var__1 ) ))
    while True:
      var__3=next(ymJoIVlh)
      if not var__4 != var__1 [ var__3 ] [ 0 ]:
        pass
      else:
        var__6 = var__6 + ( ( var__1 [ var__3 ] [ 0 ] , var__1 [ var__3 ] [ 1 ] ) , )
  except StopIteration:
    pass
  def checker ( var__5 , var__6 ) : 
    var__7 = False 
    try:
      lC=iter(range ( len ( var__5 ) ))
      while True:
        var__8=next(lC)
        var__9 = False 
        try:
          BDhu=iter(range ( len ( var__6 ) ))
          while True:
            var__10=next(BDhu)
            var__11 = ( var__5 [ var__8 ] [ 1 ] == var__6 [ var__10 ] [ 1 ] ) 
            var__9 = var__9 or var__11
        except StopIteration:
          pass
          var__7 = var__7 or var__9 
          var__7 = not var__7
    except StopIteration:
      pass
    return var__7 
  return checker ( var__5 , var__6 ) 

