first_boy = []
first_boy.append(int(input("boy1 start tree")))
first_boy.append(int(input("boy1 end tree")))

second_boy = []
second_boy.append(int(input("boy2 start tree")))
second_boy.append(int(input("boy2 end tree")))

if (first_boy[0] > second_boy[0] and first_boy[1] > second_boy[1] and first_boy[0] <= second_boy[1]):
    print((first_boy[1] - first_boy[0] + 1) + (second_boy[1] - second_boy[0] + 1) - (second_boy[1] - first_boy[0] + 1))
elif (first_boy[0]>second_boy[0] and first_boy[0] > second_boy[1]):
    print((first_boy[1]-first_boy[0]+1) + (second_boy[1]-second_boy[0]+1))
elif(second_boy[0]>first_boy[0] and first_boy[1]>second_boy[1]):
    print(first_boy[1]-first_boy[0]+1)