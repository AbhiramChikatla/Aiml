MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))



# Alpha-beta pruning is an optimization technique used in the Minimax algorithm to reduce the number of nodes
# that need to be explored in a game tree. It maintains two values, alpha and beta, to represent the best score
# achievable by the maximizer and the minimizer, respectively. If the algorithm finds a move that leads to a worse
# outcome than the current alpha or beta value, it can safely prune that part of the tree because it will not be chosen.
# This allows the algorithm to skip large portions of the game tree and significantly reduces the number of nodes
# that need to be explored, making the algorithm more efficient.


# Alpha-Beta Pruning:
# Step-1: START
# Step-2: Construct the game tree representing all possible moves and outcomes of the game.
# Step-3: Assign a score to each terminal node of the tree (i.e., the leaves) based on the outcome of the game.
# Step-4: Work back up the tree from the leaves to the root, assigning scores to each non-terminal node based on the scores
# of its children.
# Step-5: For each maximizing node, choose the child with the highest score as the optimal move and update the alpha
# value accordingly.
# Step-6: For each minimizing node, choose the child with the lowest score as the optimal move and update the beta value
# accordingly.
# Step-7: If the alpha value becomes greater than or equal to the beta value at any point during the search, prune the
# remaining children of that node and return the current score.
# Step-8: Continue recursively until the root node is reached, which represents the optimal move for the current player.