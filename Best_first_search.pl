% Define the edges of the graph (node1, node2, cost)
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(c, d, 5).
edge(d, e, 1).

% Heuristic values (node, heuristic value)
heuristic(a, 6).
heuristic(b, 2).
heuristic(c, 1).
heuristic(d, 0).
heuristic(e, 0).

% Best First Search
best_first_search(Start, Goal, Path) :-
    best_first([[Start]], Goal, Path).

% The best_first predicate takes a list of current paths, the Goal node, and returns the best path.
best_first([Path | _], Goal, Path) :-
    last(Path, Goal).

best_first([Path | Paths], Goal, FinalPath) :-
    last(Path, CurrentNode),
    findall([NextNode | Path],
            (edge(CurrentNode, NextNode, _), \+ member(NextNode, Path)),
            NewPaths),
    sort_paths(NewPaths, SortedPaths),
    append(SortedPaths, Paths, UpdatedPaths),
    best_first(UpdatedPaths, Goal, FinalPath).

% Sorting the paths based on their heuristic values
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_cost, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

% Path cost is calculated as the sum of the path's length and the heuristic of the last node
path_cost(Path, Cost) :-
    last(Path, LastNode),
    length(Path, PathLength),
    heuristic(LastNode, H),
    Cost is PathLength + H.

