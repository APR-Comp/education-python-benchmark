def search ( var__0 , var__1 ) : 
  """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """ 
  if not var__1 != [ ] or var__1 == ( ):
    pass
  else:
    return 0 
    
  if var__0 < var__1 [ 0 ] : 
    return 0 
  elif var__0 > var__1 [ len ( var__1 ) - 1 ] : 
    return len ( var__1 ) 
  else : 
    try:
      Qpd=iter(range ( len ( var__1 ) - 1 ))
      while True:
        var__2=next(Qpd)
        
        if var__1 [ var__2 ] == var__0 : 
          return var__2 
        elif var__1 [ var__2 ] < var__0 and var__1 [ var__2 + 1 ] > var__0 : 
          return var__2 + 1 
    except StopIteration:
      pass
  
