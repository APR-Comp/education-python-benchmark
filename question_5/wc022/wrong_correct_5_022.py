def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  try:
    mR=iter(range ( var__1 ))
    while True:
      var__3=next(mR)
      
      var__4 = var__0 . index ( min ( var__0 ) ) 
      var__2 . append ( var__0 . pop ( var__4 ) ) 
    
  except StopIteration:
    pass
  return var__2 

