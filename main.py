import days

y,m = list(map(int, input().split()))
# default delimiter is ' '

d = days.getDayCount(y,m)

print(d)
