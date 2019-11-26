-- shows the max value of the state
-- max temp of the state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
