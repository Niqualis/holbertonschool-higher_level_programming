-- list all cities in the hbtn_0d_usa DB
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id;
