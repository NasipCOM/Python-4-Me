def calculate_sum(N, a, b): 
  
    m1 = N / a 
    m2 = N / b

    sum = m1* (m1 + 1) / 2 + m2* (m2 + 1) / 2

    ans = a * sum + b * sum
    
    print( ans) 
  
# Driver Code 
calculate_sum(20, 3, 5)