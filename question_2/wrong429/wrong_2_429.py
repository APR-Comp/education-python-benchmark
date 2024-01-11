def unique_day ( var__0 , var__1 ) : 
  var__2 = ( ) 
  var__3 = ( ) 
  try:
    qiNjVw=iter(var__1)
    while True:
      var__4=next(qiNjVw)
      
      if not var__4 [ 1 ] in var__2:
        var__3 += ( var__4 [ 1 ] , ) 
      else:  
        var__2 += ( var__4 [ 1 ] , ) 
  except StopIteration:
    pass
  return var__0 not in var__3 
def unique_month ( var__5 , var__1 ) : 
  var__6 = ( ) 
  var__7 = ( ) 
  try:
    evPw=iter(var__1)
    while True:
      var__4=next(evPw)
      
      if not var__4 [ 0 ] not in var__6:  
       var__7 += ( var__4 [ 0 ] , ) 
      else:
        var__6 += ( var__4 [ 0 ] , ) 
  except StopIteration:
    pass
  return var__5 not in var__7 
def contains_unique_day ( var__5 , var__1 ) : 
  try:
    NGfkOLBkmxX=iter(var__1)
    while True:
      var__4=next(NGfkOLBkmxX)
      if not unique_day ( var__4 [ 1 ] , var__1 ):
        pass
      else:  
        if not var__5 == var__4 [ 0 ]:    
          continue   
        else:    
          return True 
  except StopIteration:
    pass
  finally:
    return False 
  
