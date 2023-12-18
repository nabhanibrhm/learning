with isi as
(
select 
ct.Name as "Country_Name",
count(cl.Language) as "Total_language"
from 
country ct,
countrylanguage cl
where
ct.Code = cl.CountryCode
group by ct.Name
order by count(cl.Language) desc
)
select * from isi;