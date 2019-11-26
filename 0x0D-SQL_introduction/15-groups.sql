-- updates values of second table
-- checks second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score
DESC;
