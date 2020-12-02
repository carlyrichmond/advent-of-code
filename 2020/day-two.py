def checkSchemeOne(password, letter, min, max):
    occurrences = password.count(letter)

    return occurrences in range(min, max + 1)

def checkSchemeTwo(password, letter, min, max):
    first = password[min-1]
    second = password[max-1]
    return (first == letter or second == letter) and first != second

def main(): 
    matches = 0
    
    for line in open("input/day-two.txt", "r"):
        parts = line.split(" ")
        counts = parts[0].split("-")
        
        min = int(counts[0])
        max = int(counts[1])
        letter = parts[1][0:-1]
        password = parts[2]

        # Check for max + 1 to ensure we cover max number of occurrences
        if (checkSchemeTwo(password, letter, min, max)):
            matches += 1

    print(matches)

if __name__ == "__main__":
    main()