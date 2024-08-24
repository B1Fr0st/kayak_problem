
"""
Letter layout


    k
  k a k
k a y a k
  k a k
    k

"""

letters = [
    ["","","k","",""],
    ["","k","a","k",""],
    ["k","a","y","a","k"],
    ["","k","a","k",""],
    ["","","k","",""],
]



def get_neighbors(letters, i, j):
    if i > 0:
        top = letters[i-1][j]
    else:
        top = ""
    if i < len(letters)-1:
        bottom = letters[i+1][j]
    else:
        bottom = ""
    if j < len(letters[i])-1:
        right = letters[i][j+1]  
    else:
        right = ""
    if j > 0:
        left = letters[i][j-1]
    else:
        left = ""
    return [top,bottom,right,left]

offsets = [(-1,0),(1,0),(0,1),(0,-1)]
solutions = []
for i in range(len(letters)):
    for j in range(len(letters[i])):
        current_letter = letters[i][j]
        if current_letter == "k": #Find first k
            neighbors = get_neighbors(letters,i,j)
            first_k = (i,j)
            
            for ind, neighbor in enumerate(neighbors):#Find first a
                if neighbor == "a":
                    temp_i = i+offsets[ind][0]
                    temp_j = j+offsets[ind][1]
                    first_a = (temp_i,temp_j)
                    neighbors = get_neighbors(letters,temp_i,temp_j)

                    for ind,neighbor in enumerate(neighbors):
                        if neighbor == "y": #find y
                            temp_i2 = temp_i+offsets[ind][0]
                            temp_j2 = temp_j+offsets[ind][1]
                            neighbors = get_neighbors(letters,temp_i2,temp_j2)

                            for ind,neighbor in enumerate(neighbors):
                                temp_i3 = temp_i2+offsets[ind][0]
                                temp_j3 = temp_j2+offsets[ind][1]
                                if (temp_i3,temp_j3) == first_a:
                                    continue
                                if neighbor == "a":
                                    second_a = (temp_i3,temp_j3)
                                    neighbors = get_neighbors(letters,temp_i3,temp_j3)

                                    for ind,neighbor in enumerate(neighbors):
                                        temp_i4 = temp_i3+offsets[ind][0]
                                        temp_j4 = temp_j3+offsets[ind][1]
                                        if (temp_i4,temp_j4) == first_k:
                                            continue
                                        if neighbor == "k":
                                            second_k = (temp_i4,temp_j4)
                                            solution = (first_k,first_a,(2,2),second_a,second_k)
                                            inverse_solution = (second_k,second_a,(2,2),first_a,first_k)
                                            if inverse_solution not in solutions:
                                                solutions.append(solution)
for solution in solutions:
    print(solution)
    path = [
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
    ]
    complete = ""
    for ind, index in enumerate(solution):
        complete += letters[index[0]][index[1]]
        path[index[0]][index[1]] = f"{ind+1}"
    for line in path:
        print(line)
print(f"number of permutations:{len(solutions)}") #exactly 100 lines makes my soul pure