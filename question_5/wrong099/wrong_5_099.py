def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  if var__1 >= len ( var__0 ) : 
    return False 
  elif var__1 == 1 : 
    return var__0 
  else : 
    var__3 = max ( var__0 ) 
    var__0 . remove ( var__3 ) 
    var__2 . append ( var__3 ) 
    top_k ( var__0 , var__1 - 1 ) 
    return var__2 
  pass 

