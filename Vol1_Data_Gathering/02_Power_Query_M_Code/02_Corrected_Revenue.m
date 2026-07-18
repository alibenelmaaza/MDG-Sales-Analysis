
each if [Units_Sold] = 0 then 0 
  else if [Revenue] < 0 then [Units_Sold] *30 
    else if [Revenue] < 0 and [Revenue] = 0 then 0
      else [Revenue]
