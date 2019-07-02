def save(arrivename):
    arrivename2 = list(set(arrivename))
    data = open("text.txt", 'w+')
    print(arrivename2, file=data)
    data.close()

