def main():
    
    expenses = []

    ## To run with example use day-one-example.txt as input
    for num in open("input/day-one.txt", "r"):
        expenses = expenses + [int(num)]
    
    expenses.sort()
    
    result = find_multiple(expenses)
    print(result)

def find_multiple(expenses):
    for e in expenses:
        for i in range(len(expenses)-1, 0, -1):
            if (e + expenses[i]) == 2020:
                return e * expenses[i]

if __name__ == "__main__":
    main()