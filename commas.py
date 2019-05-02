import csv
import operator


sample = open ("schedule.csv","r")

csv1 =csv.reader(sample ,delimiter=',')

sort = sorted ( csv1,key=operator.itemgetter(1))

for eachline in sort:
    print (eachline)


    def solvelist( sort , position , N ):   # so we will first check the instructores and all their signed up classes.
    # give us the list of all the positions that we have explored

        if position == ( N - 1 , N - 1 ):
            return [ ( N - 1 , N - 1 ) ]
        x , y = position


        if x + 1 < N and sort[x+1][y] == 1:   # so if x + 1 is less than N and the list ==1
            a = solvelist( sort , ( x + 1 , y ) , N )       # make a equals to the solvelist
            if a != None:
                return [ (x , y ) ] + a


        if y + 1 < N and sort[x][y+1] == 1:
            b = solvelist( sort , (x , y + 1) , N )
            if  b != None:
                return [ ( x , y ) ] + b

#section a ,section b , section c , section d , section e
#sec a = section a
      #sec a --sec b -- sec c -- sec d -- sec e
# list = [[ 1 ,   0 ,      1,      0 ,       0],
#         [ 1 ,   1 ,      0,      1 ,       0],
#         [ 0 ,   1 ,      0,      1 ,       0],
#         [ 0 ,   1 ,      0,      0 ,       0],
#         [ 1 ,   1 ,      1,      1 ,       1]
#         ]




# it will give me whenever there's a 1 , its position.

print (solvelist(sort,(0,0),5))

