from time import time  # time elapsed is now reported

BLANK = ' '
PRINT = 2000000  # this is set somewhat reasonable for 4x4 (could increase if it's producing too much output)

states_examined = 0
seen_set = set()
seen_list = []
terminals_found = 0
start_time = time()

def init_globals():
    global states_examined, seen_set, seen_list, terminals_found, start_time
    states_examined = 0
    seen_set = set()
    seen_list = []
    terminals_found = 0
    start_time = time()
  
def print_globals():
    global states_examined, seen_set, seen_list, terminals_found
    print("states / terminals / unique states / time elapsed (s)", states_examined, terminals_found, len(seen_set), time()-start_time)
    print("\n")
  
def is_terminal(state):
    blanks = state.count(BLANK)
    # BEWARE THE COMMENT AND CODE BELOW IT WHEN CHANGING to 4x4
    # a win requires at least 5 moves = <= 4 blanks
    if blanks>4: return False
    # all states filled
    if blanks==0: return True
    # check for 3 in a row
    if state[0:3]=='XXX' or state[0:3]=='OOO': return True
    if state[3:6]=='XXX' or state[3:6]=='OOO': return True
    if state[6:9]=='XXX' or state[6:9]=='OOO': return True
    # check for 3 in a column
    if state[0]+state[3]+state[6]=='XXX' or state[0]+state[3]+state[6]=='OOO': return True
    if state[1]+state[4]+state[7]=='XXX' or state[1]+state[4]+state[7]=='OOO': return True
    if state[2]+state[5]+state[8]=='XXX' or state[2]+state[5]+state[8]=='OOO': return True
    # check for 3 in a diagonal
    if state[0]+state[4]+state[8]=='XXX' or state[0]+state[4]+state[8]=='OOO': return True
    if state[2]+state[4]+state[6]=='XXX' or state[2]+state[4]+state[6]=='OOO': return True
    return False

def utility(state):
    umap = {True: 1, False: -1}
    # check for 3 in a row
    if state[0:3]=='XXX' or state[0:3]=='OOO': return umap[state[0]=='X']
    if state[3:6]=='XXX' or state[3:6]=='OOO': return umap[state[3]=='X']
    if state[6:9]=='XXX' or state[6:9]=='OOO': return umap[state[6]=='X']
    # check for 3 in a column
    if state[0]+state[3]+state[6]=='XXX' or state[0]+state[3]+state[6]=='OOO': return umap[state[0]=='X']
    if state[1]+state[4]+state[7]=='XXX' or state[1]+state[4]+state[7]=='OOO': return umap[state[1]=='X']
    if state[2]+state[5]+state[8]=='XXX' or state[2]+state[5]+state[8]=='OOO': return umap[state[2]=='X']
    # check for 3 in a diagonal
    if state[0]+state[4]+state[8]=='XXX' or state[0]+state[4]+state[8]=='OOO': return umap[state[0]=='X']
    if state[2]+state[4]+state[6]=='XXX' or state[2]+state[4]+state[6]=='OOO': return umap[state[2]=='X']
    return 0

def new_node(state):
    global states_examined, seen_set, seen_list
    states_examined += 1
    seen_set.add(state)
    # COMMENTED OUT TO SAVE MEMORY FOR THE 4x4 CASE
    # seen_list.append(state)
    if states_examined%PRINT==0:
        print("... states examined =", states_examined, ", terminals found =", terminals_found, ", unique stored =", len(seen_set), ", time elapsed (s) =", time()-start_time)
    
def next_state(state, move):
    assert state[move]==BLANK
    # BEWARE THE LINE BELOW WHEN CHANGING TO 4x4
    if state.count(BLANK)%2==1:
        turn = 'X'
    else:
        turn = 'O'
    new_state = state[:move]+turn+state[move+1:]
    return new_state

def get_available_moves(state):
    # player can move to any blank space
    return [i for i in range(len(state)) if state[i]==BLANK]

def minimax_decision(state):
    global terminals_found
    best_moves = []
    if is_terminal(state):
        terminals_found += 1
        return utility(state), best_moves
    moves = get_available_moves(state)
    best_score = float('-inf')
    for move in moves:
        new_state = next_state(state,move)
        new_node(new_state)
        score = min_value(new_state)
        if score > best_score:
            best_moves = [move]
            best_score = score
        elif score == best_score:
            best_moves.append(move)
    return best_score, best_moves

def max_value(state):
    global terminals_found
    if is_terminal(state):
        terminals_found += 1
        return utility(state)
    v = float('-inf')
    moves = get_available_moves(state)
    for move in moves:
        new_state = next_state(state,move)
        new_node(new_state)
        v = max(v, min_value(new_state))
    return v

def min_value(state):
    global terminals_found
    if is_terminal(state):
        terminals_found += 1
        return utility(state)
    v = float('inf')
    moves = get_available_moves(state)
    for move in moves:
        new_state = next_state(state,move)
        new_node(new_state)
        v = min(v, max_value(new_state))
    return v

def print_out(state):
    for r in range(3):
        for c in range(3):
            if c<2:
                endchar = '|'
            else:
                endchar = '\n'
            print(' '+state[r*3+c]+' ',end=endchar)
        if r<2:
            print(('-'*3+'+')*2+'-'*3)

test_boards = ['XXXOO'+BLANK*4,
               'OOOXX'+BLANK*4,
               BLANK*9,
               'X'+BLANK*4+'O'+BLANK*3,
               'XOO'+BLANK+'X'+BLANK*4]

for init in test_boards:
    init_globals()
    print_out(init)
    print("value of game, move =",minimax_decision(init))
    print_globals()