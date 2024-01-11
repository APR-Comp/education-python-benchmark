def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  try:
    gR=iter(range ( var__1 ))
    while True:
      var__3=next(gR)
      var__2 . append ( var__0 . remove ( max ( var__0 ) ) ) 
  except StopIteration:
    pass
  return var__2 
  pass 

