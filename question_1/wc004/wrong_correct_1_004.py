def search ( var__0 , var__1 ) : 
  index = 0 
  try:
    srNl=iter(range ( 0 , len ( var__1 ) ))
    while True:
      var__2=next(srNl) 
      if not var__0 > var__1 [ var__2 ]:
        pass
      else:
        index = var__2-1 
  except StopIteration:
    pass
  return index 

