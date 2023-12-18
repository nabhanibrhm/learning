with tes as (
SELECT
ct.Continent AS "Continent",
ct.Region AS "Region",
COUNT(ci.CountryCode) AS "Num_of_city",
row_number() over (partition by ct.Continent) as "group_num"
FROM
country ct
JOIN
city ci ON ct.Code = ci.CountryCode
where ct.Continent in('Asia','Europe')
GROUP BY
ct.Continent, ct.Region 
order by ct.Continent asc
)
select Continent, Region,Num_of_city, group_num from tes;