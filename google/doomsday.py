import math
def solution(area):
    remaining = area
    ans = []
    while(remaining > 0):
        foot = math.floor(math.sqrt(remaining))
        remaining -= (foot*foot)
        ans.append(int(foot*foot))
    return ans

print(solution(12))
print(solution(15324))