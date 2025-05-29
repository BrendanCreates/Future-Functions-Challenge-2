from typing import List, Tuple

# Basically we want to find the longest path in a DAG
# We can connect arrows between envelopes that fit
# envelops : List[Tuple[int, int, str, str]]
def max_envelope_chain(envelopes):
    # Make it so w <= h and store colors as sets
    normalized = []
    for w, h, c1, c2 in envelopes:
        if w > h:
            w, h = h, w
        color_set = {c1, c2}
        normalized.append((w, h, color_set))

    n = len(normalized)

    # Make the edges of the graph
    graph = [[] for _ in range(n)]
    for i in range(n):
        w1, h1, colors1 = normalized[i]
        for j in range(n):
            if i == j:
                continue
            w2, h2, colors2 = normalized[j]
            if w1 < w2 and h1 < h2 and colors1 & colors2:
                graph[i].append(j)

    # Use a dp array to keep track of longest path
    dp = [-1] * n

    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        max_len = 1  # Envelope itself is max length
        for v in graph[u]:
            max_len = max(max_len, 1 + dfs(v))
        dp[u] = max_len
        return dp[u]

    # Max along all nodes
    return max(dfs(i) for i in range(n))


envelopes = [
    (5, 4, "red", "blue"),
    (6, 7, "blue", "green"),
    (6, 5, "red", "green"),
    (7, 8, "blue", "yellow"),
    (4, 3, "red", "yellow"),
]

print(max_envelope_chain(envelopes))
