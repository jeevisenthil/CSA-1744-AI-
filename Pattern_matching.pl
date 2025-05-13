% Facts
color(red).
color(blue).
color(green).
color(yellow).

fruit(apple).
fruit(banana).
fruit(grape).

% Rules for matching
match_color(X) :-
    color(X), 
    write(X), 
    write(' is a valid color.'), nl.

match_fruit(X) :-
    fruit(X), 
    write(X), 
    write(' is a valid fruit.'), nl.

% General pattern matching using variables
match_pattern(FruitOrColor) :-
    color(FruitOrColor),
    write(FruitOrColor), 
    write(' is a color!'), nl.
    
match_pattern(FruitOrColor) :-
    fruit(FruitOrColor),
    write(FruitOrColor), 
    write(' is a fruit!'), nl.

% Query to check if a pattern matches a color or a fruit
query_pattern(Item) :-
    match_pattern(Item), 
    !.
query_pattern(Item) :-
    write(Item), 
    write(' does not match any known pattern.'), nl.
