def ceaser():
    nums = input("Write some numbers: ").split()
    shift = int(input("Write a shift: "))
    if shift > 0:
        for num in range(shift):
            change = nums.pop()
            nums.insert(0,change)
    else:
        for num in range(shift*(-1)):
            change1 = nums.pop(0)
            nums.append(change1)        
    print(nums)


ceaser()
 