# Solution for Eight Queens Puzzle
# Backtracking Method

rows, columns = 8,8
def illRegions(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
    
solutions = [[]]
for row in range(columns):
    solutions = (solution+[i+1]
    for solution in solutions 
    for i in range(columns)
    if not illRegions(i+1, solution))

coord = next(solutions)
coords = (list(enumerate(coord, start=1))) # Combine all results into a single list
arr = [['.' for i in range(columns)] for j in range(rows)]
for coord in coords:
    x = (coord[0] - 1) # Because the results were in xy coords,
    y = (coord[1] - 1) # needed to subtract 1 as 2D lists start
    arr[y][x] = 'Q'    # from [0][0]
for rows in arr:
    print('{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*rows))

print('Q is the location of the queens, the dots are blank spaces on the board.')
