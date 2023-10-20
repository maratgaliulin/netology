--Лекция 1: 

select 
	title,
	l."name" as "language"
from film f 
left join "language" l using(language_id);


select
	f.title,
	concat(ac.first_name, ' ', ac.last_name) as "Lambs Cincinatti Actors"
from film_actor fa 
left join actor ac using(actor_id)
left join film f using(film_id)
where fa.film_id = 508;