def top_k ( var__0 , var__1 ) : 
  var__2 = 0 
  var__3 = [ ] 
  while var__2 != var__1 : 
    var__4 = max ( var__0 ) 
    var__3 . append ( var__4 ) 
    var__0 . remove ( var__4 ) 
    var__2 += 1 
  
