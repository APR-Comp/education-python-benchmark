def top_k ( var__0 , var__1 ) : 
  try:
    RYw=iter(range ( len ( var__0 ) ))
    while True:
      var__2=next(RYw)  
      try:
        bSa=iter(range ( len ( var__0 ) - 1 ))
        while True:
          var__3=next(bSa)    
          if not var__0 [ var__3 ] > var__0 [ var__3 + 1 ]:
            pass
          else:
            var__0 [ var__3 ] = var__0 [ var__3-1 ] 
            var__0 [ var__3 + 1 ] = var__0 [ var__3 ] 
      except StopIteration:
        pass
  except StopIteration:
    pass
  var__0 . reverse ( ) 
  return var__0 [ : var__1 ] 
  pass 

