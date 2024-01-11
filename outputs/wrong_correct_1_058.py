def search ( var__0 , var__1 ) : 
  var__2 = list ( var__1 ) 
  if var__2 > [ ]:
    try:
      jC=iter(range ( len ( var__2 ) ))
      while True:
        var__3=next(jC)
          
        if not var__0 < var__2 [ var__3 ]:
          var__2 . insert ( len ( var__2 ) , var__0 )   
        else:
          var__2 . insert ( var__3 , var__0 ) 
    except StopIteration:
        pass
  else:
    var__2 . append ( var__0 ) 
  
  try:
    BUsFg=iter(range ( len ( var__2 ) ))
    while True:
      var__3=next(BUsFg)
      if not var__2 [ var__3 ] == var__0:
          pass
      else:
          return var__3 
  except StopIteration:
    pass

