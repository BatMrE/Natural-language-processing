def levenshtein_distance(w1, w2):
    d = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]

    for i in range(len(w1) + 1):
        d[i][0] = i
    for j in range(len(w2) + 1):
        d[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            c = 0 if w1[i - 1] == w2[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,  # Deletion
                d[i][j - 1] + 1,  # Insertion
                d[i - 1][j - 1] + c  # Substitution
            )

    return d[-1][-1]

# Reference : https://www.scaler.com/topics/levenshtein-distance-python/