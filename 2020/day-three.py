def generate_matrix():
    tree_map = []

    for line in open("2020/input/day-three.txt", "r"):
        tree_map = tree_map + [list(line[0:-1])]    
    
    return tree_map

def has_tree(tree_map, prior, current):
    return tree_map[current[1]][current[0]] == "#"

def main(): 
    trees = 0
    tree_map = generate_matrix()

    prior_x = 0
    prior_y = 0

    x = 0
    y = 0
    
    while (y < len(tree_map) - 1):
        prior_x = x
        prior_y = y

        x = (x + 3) % len(tree_map[y])
        y += 1

        if (has_tree(tree_map, (prior_x, prior_y), (x, y))):
            trees += 1

    print(trees)

if __name__ == "__main__":
    main()