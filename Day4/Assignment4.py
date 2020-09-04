for num in range(1042000,702648266):
  temp=num
  total_digits=len(str(temp))
  sum=0
  #print(temp)
  while temp>0:
      digit=temp%10
      sum=sum+digit**total_digits
      temp=temp//10
      if sum==num:
           print (num)
           break
      
