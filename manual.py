def findIndex(puzzle, num):
    index = puzzle.find(num)
    i = index  // 3
    j = index - i * 3
    print("i = ", i, "j = ", j)

def possibleDirection(puzzle):
    i, j = findIndex(puzzle, "0")

    map = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []
    dir = {
        (-1,0)  : "UP",
        (1,0)   : "DOWN",
        (0,-1)  : "LEFT",
        (0,1)   : "RIGHT"
    }

    for k in map:
        if not ((i+k[0] < 0) or (i+k[0] > 2) or (j+k[2] < 0) or (j+k[1] > 2)):
            result.append(dir[k])
        
        return result
    
def h_score(puzzle, goal):
    h_point = 0

    for num in range(len(puzzle)):
        i,j = findIndex(puzzle, str(num))
        x,y = findIndex(goal, str(num))

        h = abs(i-x) + abs(j-y)
        h_point += h
    
    return h_point

def gen_state(puzzle, possible_dir):
    dir = {
        "UP"    : (-1,0),
        "DOWN"  : (1,0),
        "LEFT"  : (0,-1),
        "RIGHT" : (0,1)
    }

    i,j = findIndex(puzzle, "0")

    move_to = []
    for d in possible_dir:
        move_to.append((i+dir[d][0],j+dir[d][1]))
    print(move_to)

    new_puzzle = []
    for p in move_to:

        puzzle_list = []
        for a in puzzle:
            puzzle_list.append(a)

        blank_indx = i * 3 + j
        dest_index = p[0] * 3 + p[1]

        puzzle_list[blank_indx],puzzle_list[dest_index] = puzzle_list[dest_index],puzzle_list[blank_indx]

        new_puzzle.append("".join(puzzle_list))
    
    # print(new_puzzle)
    # for b in range(len(possible_dir)):
    #     print("\n" + possible_dir[b])
    #     show_puzzle(new_puzzle[b])

    return new_puzzle

def show_puzzle(route):
    for i in range(len(route)):
        puzzle = route[i][0]
        text = route[i][1]
        g = i
        h = route[i][2]
        f = g + h
        print("Step {}: {}| g = {} h = {} f = {}".format(i, text, g, h, f))
        # print(puzzle)
        for k in range(0, 9, 3):
            print(puzzle[k] + " " + puzzle[k+1] + " " + puzzle[k+2])
        
        print("")

def solve(puzzle, goal):
    path = []
    result = []
    check = {puzzle:1}
    gen = 0
    dept = 0

    path.append([[puzzle, "START", h_score(puzzle, goal)]])
    # print(path)

    while path:
        if gen % 1000 == 0:
            print("Gen: ", gen)
        gen +- 1

        current_route = path.pop(0)
        current_puzzle = current_route[-1][0]

        if current_puzzle == goal:
            route = current_route
            return route
        
        g = len(current_route)

        if check[current_puzzle] != g:
            continue

        next_state = gen_state(current_puzzle, possible_dir(current_puzzle))

        # 
        for state in next_state:

            state_puzzle = state[0]
            state_g = g + 1

            if state_puzzle in check:

                if state_g < check[state_puzzle]:
                    check[state_puzzle] = state_g
                    to_add_state = copy.deepcopy(current_route)
                    state.append(h_score(state_puzzle,goal))
                    to_add_state.append(state)

                    path.append(to_add_state)
                
                else:
                    check[state_puzzle] = state_g
                    to_add_state = copy.deepcopy(current_route)
                    state.append(h_score(state_puzzle, goal))
                    to_add_state.append(state)
                    path.append(to_add_state)
                
                path = sorted(path, key= lambda x: (len(x), x[-1][-1]))
            pass