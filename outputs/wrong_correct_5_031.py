def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  while var__0 : 
    var__3 = var__0 [ -3 ] 
    try:
      mP=iter(var__0)
      while True:
        var__4=next(mP)   
        if not var__3 < var__4:
          pass
        else:
          var__3 = var__4 
    except StopIteration:
      pass
    var__0 . remove ( var__3 ) 
    var__2 . append ( var__3 ) 
  return var__2 [ 0 : var__1 ] 

