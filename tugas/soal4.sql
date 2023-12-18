with SC1 as (
select
	ct.continent,
    SUM(ci.population) AS 'Total_Capital_Population',
    AVG(ct.GNP) AS 'Avarage_GNP',
    rank() over (order by SUM(ci.population) desc) as "Rank_Population",
    rank() over (order by AVG(ct.GNP) desc) as "Rank_GNP"
from country ct, city ci
where
ct.Capital = ci.id
group by ct.Continent
order by SUM(ci.population) desc
)
select continent, Total_Capital_Population, Avarage_GNP, Rank_Population, Rank_GNP
from SC1;