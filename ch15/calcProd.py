import time
def calcProd():
    #calculate the proeduct of the first 100,000 numbers.
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s didgits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
