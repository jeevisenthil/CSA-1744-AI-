% Define vowel facts
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(A) :- vowel(a).
vowel(E) :- vowel(e).
vowel(I) :- vowel(i).
vowel(O) :- vowel(o).
vowel(U) :- vowel(u).

% Base case: an empty list has 0 vowels
count_vowels([], 0).

% Recursive case: check the first character and count vowels
count_vowels([Head|Tail], Count) :-
    (vowel(Head) -> 
        count_vowels(Tail, TailCount), 
        Count is TailCount + 1 ; 
        count_vowels(Tail, Count)).

% Helper predicate to count vowels in a string (converts string to list)
count_vowels_in_string(String, Count) :-
    string_chars(String, CharList),
    count_vowels(CharList, Count).
