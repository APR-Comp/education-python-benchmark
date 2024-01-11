def top_k ( var__0 , var__1 ) : 
  var__2 = [ ] 
  var__3 = 0 
  while var__3 < var__1 : 
    try:
      kcwBgMU=iter(range ( - len ( var__0 ) , 0 ))
      while True:
        var__4=next(kcwBgMU)
        
        if not var__0 [ var__4 ] == max ( var__0 ):
          pass
        else:  
          var__2 . append ( var__0 . pop ( var__4 ) ) 
          var__3 += 1 
    except StopIteration:
      pass
  return var__2 

