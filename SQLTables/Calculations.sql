-- Calculate the percentage of homeownership by income group for a specific year:
SELECT homeownership, income, (total * 100.0 / SUM(total) OVER (PARTITION BY year)) AS percentage
FROM homeownership
WHERE year = 2021; -- Change the year as needed

-- Calculate the total number of homeowners by age group for a specific year:
SELECT age, SUM(total) AS total_homeowners
FROM homeownership
WHERE year = 2021 -- Change the year as needed
GROUP BY age;

-- Calculate the percentage of homeownership by age group for a specific year:
SELECT age, (total * 100.0 / SUM(total) OVER (PARTITION BY year)) AS percentage
FROM homeownership
WHERE year = 2021; -- Change the year as needed

-- Calculate the change in the total number of homeowners from one year to the next:
SELECT year, total - LAG(total) OVER (ORDER BY year) AS change
FROM homeownership;
