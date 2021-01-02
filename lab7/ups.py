def golden_max_slice(A):
  max_ending = max_slice = 0
  for a in A:
    max_ending = max(0, max_ending + a)
    max_slice = max(max_slice, max_ending)
  return max_slice

A = [1,2,-2,4,5,6,2,8]
print(sum(A))
print(golden_max_slice(A))