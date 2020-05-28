switchs = 10
lamps = [False]*switchs
trips = 8

def main():

    for t in range(1,trips+1) :
        if t%3 == 1:
            switch_lamps(1)
        if t%3 == 2:
            switch_lamps(2)
        if t%3 == 0:
            switch_lamps(3) 
    print(lamps.count(True))
        
def switch_lamps(n):
    loop = n
    while loop <= switchs:
        lamps[loop-1] = nand(lamps[loop-1], True)
        loop += n

def nand(value1, value2):
    return not(value1 and value2)

main()
