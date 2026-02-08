# backend/app/patterns/chess_map.py

from typing import Dict
from app.patterns.registry import DSAPattern

CHESS_PATTERN_MAP: Dict[DSAPattern, str] = {
    DSAPattern.TWO_POINTERS: (
        "Like two rooks closing in from opposite files. "
        "Each move reduces space until the truth is forced."
    ),

    DSAPattern.SLIDING_WINDOW: (
        "A king patrolling a fixed territory. "
        "The window moves, but its size and rules stay controlled."
    ),

    DSAPattern.HASHING: (
        "Piece coordination. You trade space for memory, "
        "placing pieces so you never have to search blindly."
    ),

    DSAPattern.RECURSION: (
        "Opening theory. You trust the structure. "
        "Each position solves a smaller version of the same idea."
    ),

    DSAPattern.BINARY_SEARCH: (
        "A classic divide-and-conquer attack. "
        "Every move cuts the board in half, removing uncertainty."
    ),

    DSAPattern.PREFIX_SUM: (
        "Pre-calculated pressure. The work is done early "
        "so later positions resolve instantly."
    ),

    DSAPattern.STACK: (
        "Last piece moved must resolve first. "
        "Tension builds until it can unwind cleanly."
    ),

    DSAPattern.QUEUE: (
        "Orderly development. Pieces activate in the exact "
        "sequence they were prepared."
    ),

    DSAPattern.TREE_DFS: (
        "A deep calculation line. You follow one variation "
        "to its conclusion before considering alternatives."
    ),

    DSAPattern.TREE_BFS: (
        "A wide positional scan. You examine all immediate threats "
        "before committing deeper."
    ),

    DSAPattern.GRAPH_DFS: (
        "Exploring a tangled middlegame variation deeply, "
        "marking where you've already been to avoid loops."
    ),

    DSAPattern.GRAPH_BFS: (
        "Finding the shortest tactical path. "
        "Distance matters more than depth."
    ),

    DSAPattern.GREEDY: (
        "Grabbing the best-looking move now, "
        "trusting that local advantage leads to global victory."
    ),

    DSAPattern.DYNAMIC_PROGRAMMING: (
        "Endgame tablebases. You store solved positions "
        "so you never calculate the same ending twice."
    ),
}


def get_chess_analogy(pattern: DSAPattern) -> str:
    """
    Returns the chess analogy for a given DSA pattern.
    """
    return CHESS_PATTERN_MAP.get(
        pattern,
        "An unfamiliar position. No known pattern applies yet."
    )