# import csv
#
# with open('schedule.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(row)
#
# csvFile.close()


# def permutations(list,start,end):
#     if (start == end):
#         print(list)
#     else:
#         for i in range (start,end + 1):
#             list[start], list[i] = list[i], list[start]  # The swapping
#             permutations(list, start + 1, end)
#             list[start], list[i] = list[i], list[start]  # Backtracking
#
# permutations([1, 2, 3], 0, 2)
"""

If we have reached the destination point
        return an array containing only the position of the destination
else
       a,move in the forwards direction and check if this leads to a solution
       b,if  option a does not work, then move down
      c, if either work, add the current position to the solution obtained at either a or b

"""
def solvelist( list , position , N ):   # so we will first check the instructores and all their signed up classes.
    # give us the list of all the positions that we have explored

    if position == ( N - 1 , N - 1 ):
        return [ ( N - 1 , N - 1 ) ]
    x , y = position


    if x + 1 < N and list[x+1][y] == 1:   # so if x + 1 is less than N and the list ==1
        a = solvelist( list , ( x + 1 , y ) , N )       # make a equals to the solvelist
        if a != None:
            return [ (x , y ) ] + a


    if y + 1 < N and list[x][y+1] == 1:
        b = solvelist( list , (x , y + 1) , N )
        if  b != None:
            return [ ( x , y ) ] + b

#section a ,section b , section c , section d , section e
#sec a = section a
      #sec a --sec b -- sec c -- sec d -- sec e
list = [[ 1 ,   0 ,      1,      0 ,       0],
        [ 1 ,   1 ,      0,      1 ,       0],
        [ 0 ,   1 ,      0,      1 ,       0],
        [ 0 ,   1 ,      0,      0 ,       0],
        [ 1 ,   1 ,      1,      1 ,       1]
        ]

# it will give me whenever there's a 1 , its position.

print (solvelist(list,(0,0),5))

"""
then check if an instructor has taken more than 2 courses. 

"""


"""
then check if every course has at least 1 instructor 

"""