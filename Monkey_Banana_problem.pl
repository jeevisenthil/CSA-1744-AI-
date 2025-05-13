% Initial State: monkey at door, box at window, monkey on floor, monkey doesn't have banana
% State format: state(MonkeyPos, BoxPos, MonkeyOnBox, HasBanana)

% Move from one place to another
move(state(MP, BP, no, no), walk(MP, NP), state(NP, BP, no, no)) :- place(NP).

% Push box to a new location
move(state(P, P, no, no), push(P, NP), state(NP, NP, no, no)) :- place(NP).

% Climb onto the box
move(state(P, P, no, no), climb, state(P, P, yes, no)).

% Grab the banana
move(state(middle, middle, yes, no), grab, state(middle, middle, yes, yes)).

% Places in the room
place(door).
place(window).
place(middle).

% Monkey can reach banana if there's a sequence of moves from initial to goal state
can_get_banana :- 
    moves(state(door, window, no, no), state(_, _, _, yes), []).

% Try different moves recursively
moves(State, State, _).
moves(CurrentState, GoalState, Visited) :-
    move(CurrentState, _, NextState),
    \+ member(NextState, Visited),
    moves(NextState, GoalState, [NextState|Visited]).
