def remove_extras ( var__0 ) : 
  var__1 = [ ] 
  if var__0 == [ ] : 
    return var__1 
  elif var__0 [ 0 ] in var__1 : 
    return var__1 + remove_extras ( var__0 [ 1 : ] ) 
  else : 
    var__1 += [ var__0 [ 0 ] ] 
    return var__1 + remove_extras ( var__0 [ 1 : ] ) 
  
