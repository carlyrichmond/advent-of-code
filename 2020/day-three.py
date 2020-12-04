def generate_matrix():
    tree_map = []

    for line in open("2020/input/day-three.txt", "r"):
        tree_map = tree_map + [list(line.strip("\n"))]    
    
    return tree_map

def has_tree(tree_map, prior, current):
    return tree_map[current[1]][current[0]] == "#"

def main(): 
    result = 1 # One to ensure the multiplication isn't cancelled out initially
    tree_map = generate_matrix()
    
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        prior_x = 0
        prior_y = 0

        x = 0
        y = 0

        trees = 0

        while (y < len(tree_map) - 1):
            prior_x = x
            prior_y = y

            y += slope[1]
            x = (x + slope[0]) % len(tree_map[y])
            
            if (has_tree(tree_map, (prior_x, prior_y), (x, y))):
                trees += 1

        result *= trees

    print(result)

if __name__ == "__main__":
    main()