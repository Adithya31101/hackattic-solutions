def solution(h, q):
  ans = []

  for n in q:
    start = 1
    end = int((2**h) - 1)
    if n < start or n >= end:
      ans.append(-1)
      continue
    while(True):
      end -= 1
      mid = start + (end - start) // 2
      if mid == n or end == n:
        ans.append(end + 1)
        break
      elif n < mid:
        end = mid
      else:
        start = mid

  return ans

print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))