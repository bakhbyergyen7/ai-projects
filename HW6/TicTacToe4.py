from time import time  # time elapsed is now reported

BLANK = '-'
PRINT = 10000000  # this is set somewhat reasonable for 4x4 (could increase if it's producing too much output)

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
    # a win requires at least 6 moves = <= 6 blanks
    if blanks > 5:
        return False
    # all states filled
    if blanks == 0:
        return True
    # check for 4 in a row
    if state[0:4] == 'XXXX' or state[0:4] == 'OOOO':
        return True
    if state[4:8] == 'XXXX' or state[4:8] == 'OOOO':
        return True
    if state[8:12] == 'XXXX' or state[8:12] == 'OOOO':
        return True
    if state[12:16] == 'XXXX' or state[12:16] == 'OOOO':
        return True
    # check for 4 in a column
    if state[0] + state[4] + state[8] + state[12] == 'XXXX' or state[0] + state[4] + state[8] + state[12] == 'OOOO':
        return True
    if state[1] + state[5] + state[9] + state[13] == 'XXXX' or state[1] + state[5] + state[9] + state[13] == 'OOOO':
        return True
    if state[2] + state[6] + state[10] + state[14] == 'XXXX' or state[2] + state[6] + state[10] + state[14] == 'OOOO':
        return True
    if state[3] + state[7] + state[11] + state[15] == 'XXXX' or state[3] + state[7] + state[11] + state[15] == 'OOOO':
        return True
    # check for 4 in a diagonal
    if state[0] + state[5] + state[10] + state[15] == 'XXXX' or state[0] + state[5] + state[10] + state[15] == 'OOOO':
        return True
    if state[3] + state[6] + state[9] + state[12] == 'XXXX' or state[3] + state[6] + state[9] + state[12] == 'OOOO':
        return True
    return False


def utility(state):
    umap = {True: 1, False: -1}
    # check for 4 in a row
    if state[0:4]=='XXXX' or state[0:4]=='OOOO': return umap[state[0]=='X']
    if state[4:8]=='XXXX' or state[4:8]=='OOOO': return umap[state[4]=='X']
    if state[8:12]=='XXXX' or state[8:12]=='OOOO': return umap[state[8]=='X']
    if state[12:16]=='XXXX' or state[12:16]=='OOOO': return umap[state[12]=='X']
    # check for 4 in a column
    if state[0]+state[4]+state[8]+state[12]=='XXXX' or state[0]+state[4]+state[8]+state[12]=='OOOO': return umap[state[0]=='X']
    if state[1]+state[5]+state[9]+state[13]=='XXXX' or state[1]+state[5]+state[9]+state[13]=='OOOO': return umap[state[1]=='X']
    if state[2]+state[6]+state[10]+state[14]=='XXXX' or state[2]+state[6]+state[10]+state[14]=='OOOO': return umap[state[2]=='X']
    if state[3]+state[7]+state[11]+state[15]=='XXXX' or state[3]+state[7]+state[11]+state[15]=='OOOO': return umap[state[3]=='X']
    # check for 4 in a diagonal
    if state[0]+state[5]+state[10]+state[15]=='XXXX' or state[0]+state[5]+state[10]+state[15]=='OOOO': return umap[state[0]=='X']
    if state[3]+state[6]+state[9]+state[12]=='XXXX' or state[3]+state[6]+state[9]+state[12]=='OOOO': return umap[state[3]=='X']
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
    for r in range(4):
        for c in range(4):
            if c<3:
                endchar = '|'
            else:
                endchar = '\n'
            print(' '+state[r*4+c]+' ',end=endchar)
        if r<3:
            print(('-'*4+'+')*3+'-'*4)

test_boards = ['XXXO'+BLANK*3+'OOO'+BLANK*4,
               'OOOX'+BLANK*3+'XXOO'+BLANK,
               BLANK*16,
               'X'+BLANK*4+'O'+BLANK*3+'X'+BLANK*4,
               'XOO'+BLANK+'X'+BLANK*3+'O'+BLANK*3+'X'+BLANK]




for init in test_boards:
    init_globals()
    print_out(init)
    print("value of game, move =",minimax_decision(init))
    print_globals()