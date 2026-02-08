# backend/app/patterns/registry.py

from enum import Enum
from typing import List


class DSAPattern(str, Enum):
    TWO_POINTERS = "two_pointers"
    SLIDING_WINDOW = "sliding_window"
    HASHING = "hashing"
    RECURSION = "recursion"
    BINARY_SEARCH = "binary_search"
    PREFIX_SUM = "prefix_sum"
    STACK = "stack"
    QUEUE = "queue"
    TREE_DFS = "tree_dfs"
    TREE_BFS = "tree_bfs"
    GRAPH_DFS = "graph_dfs"
    GRAPH_BFS = "graph_bfs"
    GREEDY = "greedy"
    DYNAMIC_PROGRAMMING = "dynamic_programming"


def all_patterns() -> List[str]:
    """
    Returns all supported DSA patterns as strings.
    Used to constrain Gemini responses.
    """
    return [pattern.value for pattern in DSAPattern]