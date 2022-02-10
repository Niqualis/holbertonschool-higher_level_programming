-- list all cities of Cali found in the DB
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY id;
