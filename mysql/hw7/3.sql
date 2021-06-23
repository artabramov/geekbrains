SELECT flights.id FROM flights
LEFT JOIN cities.name AS from ON cities.label=flights.from
LEFT JOIN cities.name AS to ON cities.label=flights.to;
