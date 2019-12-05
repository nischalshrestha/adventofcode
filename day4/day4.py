
low = 172930
high = 683082

# part 1 was on my own and is very fiddly :D
total = 0
for idx in range(low, high+1):
    i = 0
    j = i + 1
    number = str(idx)
    double = 0
    decrease = 0
    for s in range(len(number)-1):
        l, r = number[i], number[j]
        if l == r:
            double += 1
        if decrease == 0 and r < l:
            decrease += 1
        i += 1
        j += 1
    if double > 0 and decrease != 1:
        total += 1
print(total)

# this one annoyed me so got help from subreddit
total = 0
for idx in range(low, high+1):
    number = [int(s) for s in str(idx)]
    # comparing to sorted version means it can rule out ones where it violates
    # decreasing and having at least one other double rules
    if number != sorted(number): continue 
    for d in number:
        if number.count(d) == 2:
            total += 1
            break

print(total)
    