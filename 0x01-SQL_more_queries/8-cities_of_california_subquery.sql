-- list all cities of Cali found in the DB
SELECT id, NAME FROM cities WHERE state_id = (select id FROM states WHERE name = 'california')
ORDER BY id;
