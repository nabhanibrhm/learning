WITH CountryPercentage AS (
    SELECT
        ct1.name,
        (ct1.GNP / (SELECT SUM(ct1.GNP) FROM country ct1))*100 AS percentage,
        (SELECT SUM(ct2.GNP / (SELECT SUM(ct2.GNP) FROM country ct2) * 100)
         FROM country ct2 
         WHERE ct1.GNP <= ct2.GNP) AS cumulative_consumption
    FROM
        country ct1
)
SELECT
    name,
    percentage,
    cumulative_consumption,
    RANK() OVER (ORDER BY percentage DESC) AS country_rank,
    NTILE(4) OVER (ORDER BY percentage DESC) AS market_prority
FROM
    CountryPercentage
WHERE cumulative_consumption <= 81
ORDER BY
    percentage DESC;
