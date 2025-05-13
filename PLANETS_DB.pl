% Facts: planet(Name, Diameter_km, DistanceFromSun_million_km, Moons)

planet(mercury, 4879, 58, 0).
planet(venus, 12104, 108, 0).
planet(earth, 12742, 150, 1).
planet(mars, 6779, 228, 2).
planet(jupiter, 139820, 778, 79).
planet(saturn, 116460, 1429, 82).
planet(uranus, 50724, 2871, 27).
planet(neptune, 49244, 4495, 14).

% Rules

% Find planets with more than N moons
many_moons(N, Name) :-
    planet(Name, _, _, Moons),
    Moons > N.

% Find planets closer than a given distance (in million km)
closer_than(Distance, Name) :-
    planet(Name, _, Dist, _),
    Dist < Distance.
