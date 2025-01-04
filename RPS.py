def player(prev_play, opponent_history=[]):
    """
    Enhanced function for playing Rock-Paper-Scissors.
    Tracks opponent's play history and attempts to predict their next move.
    """
    # Append opponent's previous move to history
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize a counter for opponent's move sequences
    n = 3  # Length of sequence to analyze
    if len(opponent_history) < n:
        return "R"  # Default move for the first few rounds

    # Build a sequence dictionary to track opponent's patterns
    sequence = "".join(opponent_history[-n:])
    sequence_dict = {}

    for i in range(len(opponent_history) - n):
        key = "".join(opponent_history[i:i + n])
        next_move = opponent_history[i + n]
        if key not in sequence_dict:
            sequence_dict[key] = {"R": 0, "P": 0, "S": 0}
        sequence_dict[key][next_move] += 1

    # Predict the opponent's next move based on the sequence
    if sequence in sequence_dict:
        prediction = max(sequence_dict[sequence], key=sequence_dict[sequence].get)
    else:
        prediction = "R"  # Default prediction

    # Return the counter move to the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[prediction]
