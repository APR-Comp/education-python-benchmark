def sort_age ( var__0 ) : 
  var__1 = var__0 
  var__2 = [ ] 
  while var__1 : 
    var__3 = var__1 [ 0 ] 
    try:
      EDkaPw=iter(var__1)
      while True:
        var__4=next(EDkaPw)
          
        if not var__4 [ 0 ] < var__3 [ 1 ]:
            pass
        else:
            var__3 = var__4 
    except StopIteration:
        pass
    var__1 . remove ( var__3 ) 
    var__2 . append ( var__3 ) 
  var__2 . reverse ( ) 
  return var__2 

