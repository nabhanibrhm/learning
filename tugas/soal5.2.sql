with total_populasi as (
SELECT 
    ct.Name,
    ct.GovernmentForm,
    (select sum(Population) from country) as total,
    (ct.Population / (SELECT SUM(Population) FROM Country)) * 100 AS PercentagePopulation,
    ROW_NUMBER() OVER (ORDER BY ct.Name) AS Row_Index

FROM Country ct
group by ct.Name, ct.GovernmentForm,ct.Population

order by PercentagePopulation desc
)
select * from total_populasi limit 10;




with total_populasi as (
SELECT 
    ct.continent,
    ct.region,
    (select count(city) from country) as number_of_city,
    ROW_NUMBER() OVER (ORDER BY ct.Name) AS Row_Index
FROM Country ct
where ct.continent = 'Europe' and 'Asia'
group by ct.Name, ct.GovernmentForm,ct.Population

order by PercentagePopulation desc
)
select * from total_populasi limit 10;
