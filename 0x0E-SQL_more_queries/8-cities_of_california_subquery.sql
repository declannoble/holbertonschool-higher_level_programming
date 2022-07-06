-- script to create cities connected to state in db

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
    )
ORDER BY id ASC
