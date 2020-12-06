def main():
    
    expenses = []

    ## To run with example use day-one-example.txt as input
    for num in open("2020/1/day-one.txt", "r"):
        expenses = expenses + [int(num)]
    
    expenses.sort()
    
    result = find_three_multiples(expenses)
    print(result)

def find_multiple(expenses):
    for e in expenses:
        for i in range(len(expenses)-1, 0, -1):
            if (e + expenses[i]) == 2020:
                return e * expenses[i]

def find_three_multiples(expenses):
    for e in expenses:
        for f in expenses:
            for i in range(len(expenses)-1, 2, -1):
                if (e + f + expenses[i]) == 2020:
                    return e * f * expenses[i]

if __name__ == "__main__":
    main()