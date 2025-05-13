% Facts: These are known facts in the knowledge base.
person(john).
person(mary).
person(jane).
person(paul).

% Facts about relationships: these describe who is a parent of whom.
parent(john, mary).
parent(john, jane).
parent(mary, paul).

% Rules: Rules that help deduce new facts.

% Rule to find if someone is a grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Backward Chaining for Grandparent
% The goal is to find if X is a grandparent of Y.
backward_chaining(Goal) :-
    Goal, % Try to prove the goal
    write('Goal: '), write(Goal), nl.
