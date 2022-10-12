n = int(input())
e = list(map(int, input().split()))
recruits = 0
untreated_events = 0
 
for i in e:
    if i > 0:
        recruits += i
    else:
        recruits += i
        if recruits < 0:
            untreated_events += 1
            recruits = 0
 
print(untreated_events)
