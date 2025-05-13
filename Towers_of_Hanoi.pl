% hanoi(N, Source, Destination, Auxiliary)
hanoi(1, Src, Dest, _) :-
    format('Move disk from ~w to ~w~n', [Src, Dest]).
hanoi(N, Src, Dest, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, Src, Aux, Dest),
    hanoi(1, Src, Dest, _),
    hanoi(M, Aux, Dest, Src).
