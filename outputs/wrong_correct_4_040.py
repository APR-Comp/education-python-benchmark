def sort_age ( var__0 ) : 
  try:
    zF=iter(range ( 0 , len ( var__0 ) ))
    while True:
      var__1=next(zF)
      var__2 = var__0 [ var__1 ] 
      var__3 = 0 
      while var__3 > var__1 : 
        if not var__2 [ 1 ] > var__0 [ var__3 ] [ 1 ]:
          pass
        else:
          break
        var__3 += 1 
      del var__0 [ var__1 ] 
      var__0 . insert ( var__3 , var__2 )
  except StopIteration:
    pass
  return var__0 

