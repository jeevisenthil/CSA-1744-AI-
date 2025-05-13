% Facts
bird(sparrow).
bird(penguin).
bird(eagle).
bird(ostrich).
bird(parrot).

% Facts about flight ability
cannot_fly(penguin).
cannot_fly(ostrich).

% Rule: A bird can fly if it is a bird and not listed in cannot_fly
can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).

% Rule: A bird cannot fly if it's listed in cannot_fly
cannot_fly_bird(Bird) :-
    bird(Bird),
    cannot_fly(Bird).
