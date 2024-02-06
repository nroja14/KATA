def squares(numbers, s: int):
    ss = str(s) + str(s)
    limit = int(ss)
    squaresArray = []
    for n in numbers:
        sqare = n * n
        if sqare <= limit and len(squaresArray) == 0:
            squaresArray.append(sqare)
        elif sqare == 0:
            squaresArray.insert(0, sqare)
        elif sqare <= limit:
            lastElementIndex = len(squaresArray) - 1
            lastElement = squaresArray[lastElementIndex]
            squaresArray.append(sqare) if sqare >= lastElement else squaresArray.insert(lastElementIndex, sqare)
    return squaresArray


#numbers =  [-6, -2, 0, 3, 7]   
#numbers =  [1, 2, 3, 5, 6, 8, 9]
#numbers = [-2, 1]
numbers =  [-6, -5, 0, 5, 6]
print(squares(numbers, 6))