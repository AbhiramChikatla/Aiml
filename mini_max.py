import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

# Example scores at the leaf nodes
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Calculate tree depth (log base 2 of number of scores)
treeDepth = int(math.log2(len(scores)))

print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))


# Description
# The Minimax algorithm is a decision-making algorithm used in game theory and artificial intelligence. It is used
# to determine the best move for a player in a two- player zero-sum game where the outcome depends on the
# choices made by both players. The algorithm works by exploring the game tree to a certain depth, assigning a
# score to each possible outcome, and selecting the move that minimizes the maximum loss. The algorithm
# alternates between maximizing and minimizing phases, and while it is effective for determining the best move, it
# can be computationally expensive for large game trees. Improvements such as alpha-beta pruning can be used to
# improve its efficiency.

# Algorithm
# Step-1: Start
# Step-2: Construct the game tree representing all possible moves and outcomes of the game.
# Step-3: Assign a score to each terminal node of the tree (i.e., the leaves) based on the outcome of the game.
# Step-4: Work back up the tree from the leaves to the root, assigning scores to each non-terminal node based on the scores
# of its children.
# Step-5: For each maximizing node, choose the child with the highest score as the optimal move.
# Step-6: For each minimizing node, choose the child with the lowest score as the optimal move.
# Step-7: Continue recursively until the root node is reached, which represents the optimal move for the current player.
# Step-8 : END


