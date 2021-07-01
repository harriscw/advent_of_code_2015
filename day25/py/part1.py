import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

#some initial values
thisval = 20151125
row = 1
col = 1
maxrow=1

while True:
    # if row==1 and col==1:
    #     print(row,col,thisval)
    if row==1:#go back to column one, down a row from the previous max row in column 1
        row=maxrow+1
        maxrow+=1
        col=1
    else:#otherwise go up diagonally until you get to the first row
        row-=1
        col+=1
    thisval = (thisval*252533) % 33554393 #find the value at this position
    #print(row,col,thisval)
    if row==2947 and col==3029:#output when you get to the row of interest
        print("Final Answer",thisval)
        break

print("Start:",start,"End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Total Time Elapsed:",round(time.time()-startsec,5))