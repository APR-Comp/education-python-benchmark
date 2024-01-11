def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  try:
    khVpcOD=iter(range ( var__1 ))
    while True:
      var__3=next(khVpcOD)
      var__2 . append ( max ( var__0 ) ) 
      var__0 . remove ( max ( var__0 ) ) 
    
  except StopIteration:
    pass
  return var__2