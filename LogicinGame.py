import random


# it will create new matrix with 0's everytime when we will call start_game
# let we denote the empty places/values by 0's
def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


# When we want to add new 2 in the matrix we will call this function and pass the matrix in which we want to add 2
def add_new_2(mat):
    # we have to generate 2 at random position where there is 0
    r = random.randint(0, 3)  # here we generate a random number for row
    c = random.randint(0, 3)  # here we generate a random number for column
    while (mat[r][c] != 0):  # we will keep doing this until we get a position where 0 is present
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


def reverse(mat):  # it will reverse only rows of the matrix
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4 - j - 1])
    return new_mat


def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# We need to compress it i.e move all the numbers to left side this logic for the left move
def compress(mat):
    new_mat = []  # we have to return a new matrix in this function
    changed = False
    for i in range(4):
        new_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][
                j] != 0:# if at any position there is not empty value then we have to shift it to new column in the same row
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1  # we will increment pos when we encounter non-zero value and for next non zero value it should store the info
    return new_mat, changed


# we have to merge/combine all non-zero no which are equal to the no next(up,down,left,right) to it,this logic for the left move
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2  # the no after merging becomes double of its previous
                mat[i][j + 1] = 0  # After combining the next value is becoming zero
                changed = True
    return mat, changed


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2  # if any compression or merging happens it will be true
    new_grid, temp = compress(new_grid)
    return new_grid, changed


def move_right(grid):  # we will use the same logic as that of left but only positions and indexes logic is change
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2  # if any compression or merging happens it will be true
    new_grid, temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, changed


def move_down(grid):  # we will use the same logic as that of left but only positions and indexes logic is change
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2  # if any compression or merging happens it will be true
    new_grid, temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid, changed


def move_up(grid):  # we will use the same logic as that of left but only positions and indexes logic is change
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2  # if any compression or merging happens it will be true
    new_grid, temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid, changed


# We want to have current state of game at each point i.e we want to know whether we won the game,loss the game or game not over yet
def get_current_state(mat):
    # we will won the match if at any position in matrix we get the no 2048
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return 'WON'
    # We would be still in the game if at any position there 0 is present i.e matrix is not completely filled
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'
    # Another condition for which we would be still in the game will be when there will be combination of no's possible
    for i in range(3):  # we are taking range 3 to avoid index out of range error for last column or last row values
        for j in range(3):
            if (mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]):
                return 'GAME NOT OVER'
    # in above case we have't check for last row or last column values so we have to check
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:  # For last row
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:  # For last column
            return 'GAME NOT OVER'
    # IF neither of the above conditions satisfied it means we have lost the game
    return 'LOST'

#mat=start_game()
#add_new_2(mat)
#add_new_2(mat)
#print(mat)
#mat,temp=move_up(mat)
#print(mat)
#mat,temp=move_right(mat)
#print(mat)
#add_new_2(mat)
#print(mat)
#mat,temp=move_down(mat)
#print(mat)
#mat,temp=move_left(mat)
#print(mat)
#mat,temp=move_down(mat)
#print(mat)