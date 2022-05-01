def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

# Test code
for i in range(50):
  if is_prime(i):
      print(i)