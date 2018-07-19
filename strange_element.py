import sys

s1 = list(map(int, input().split())) # s1 is the bigger array
s2 = list(map(int, input().split())) # s2 is the smaller array

g = []

minn_sum = sys.maxsize
ind_minn_sum = -1
for blocked in range(len(s1)):
    summ = 0
    s2_ind = 0
    for s1_ind in range(len(s1)):
        if s1_ind == blocked:
            continue
          
        summ += abs(s1[s1_ind] - s2[s2_ind])
        s2_ind += 1

    if summ < minn_sum:
        minn_sum = summ
        ind_minn_sum = blocked

# ind_minn_sum contains the indice to the element from s1 that is more possible
# to be a strange element when you want to match s1 elements to s2 elements.
del s1[ind_minn_sum]

print(s1)
print(s2)


        
