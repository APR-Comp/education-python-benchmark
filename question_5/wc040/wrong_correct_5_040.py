def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  while var__0 : 
    var__3 = var__0 [ 0 ] 
    try:
        fN=iter(var__0)
        while True:
          var__4=next(fN)
          if not var__4 < var__3:
            pass
          else:
            var__3 = var__4 
    except StopIteration:
      pass
    var__0 . remove ( var__3 ) 
    var__2 . append ( var__3 ) 
  return var__2 [ : var__1 ] 

