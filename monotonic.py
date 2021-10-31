def is_monotonic(nums):
    P=[]
    P.extend(nums)
    Q = []
    Q.extend(nums)
    P.sort()
    Q.reverse()
    if nums == P:
        return True
    elif P == O:
        return True
    else:
        return False
nums = []
print('...')
nums = input('nums = ')
A = nums[1:-1]
S = (A.split(','))
i = iter(S)
L = list(iter(lambda: int(next(i)), None))
print(is_monotonic(L))
