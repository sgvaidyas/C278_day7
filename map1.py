marks = [90,50,30,40,60]
def getExtraMarks(m):
    return m +5
final_marks = map(getExtraMarks, marks)

finalmarks2 = map(lambda x:x+5,marks)
print(list(final_marks))
print(list(finalmarks2))
