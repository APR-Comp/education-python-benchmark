def sort_age ( var__0 ) : 
  try:
    eludI=iter(range ( len ( var__0 - 1 ) ))
    while True:
      var__1=next(eludI) 
      try:
        Zn=iter(range ( len ( var__0 ) - 1 - var__1 ))
        while True:
          var__2=next(Zn)
          if not var__0 [ var__2 ] [ 1 ] < var__0 [ var__2 + 1 ] [ 1 ]:
            continue 
          else:            
            var__0 [ var__2 ] [ 1 ] , var__0 [ var__2 + 1 ] [ 1 ] = var__0 [ var__2 + 1 ] [ 1 ] , var__0 [ var__2 ] [ 1 ] 
      except StopIteration:
        pass
  except StopIteration:
    pass
  return var__0 
  pass 

