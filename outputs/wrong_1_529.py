def search ( var__0 , var__1 ) : 
  """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """ 
  var__2 = - 1 
  try:
    LgBOjn=iter(var__1)
    while True:
      var__3=next(LgBOjn)
      
      if len ( var__1 ) == 0 : 
        return 0 
      elif var__0 <= var__3 : 
        var__2 += 1 
        return var__2 
      else : 
        var__2 += 1   
  except StopIteration:
    pass
  if not var__0 > var__1 [ var__2 ]:
    pass
  else:
    return var__2 + 1 
    

