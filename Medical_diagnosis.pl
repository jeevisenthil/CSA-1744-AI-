% Facts about diseases and their symptoms
disease(flu, [fever, cough, body_aches, sore_throat]).
disease(cold, [cough, sore_throat, runny_nose]).
disease(covid19, [fever, cough, loss_of_taste, difficulty_breathing, sore_throat]).
disease(malaria, [fever, chills, sweating, headache]).
disease(allergy, [sneezing, itchy_eyes, runny_nose]).
disease(pneumonia, [fever, cough, difficulty_breathing, chest_pain]).

% Rule to diagnose a disease based on symptoms
diagnose(Disease) :-
    write('Please enter your symptoms (type symptoms as a list, e.g., [fever, cough]): '),
    read(Symptoms),
    find_disease(Symptoms, Disease).

% Find possible diseases based on the symptoms
find_disease(Symptoms, Disease) :-
    disease(Disease, DiseaseSymptoms),
    subset(Symptoms, DiseaseSymptoms),
    format('You may have ~w. Check with a healthcare professional for confirmation.~n', [Disease]).

% Example of testing whether a set of symptoms match
subset([], _).
subset([X|XS], YS) :- member(X, YS), subset(XS, YS).
