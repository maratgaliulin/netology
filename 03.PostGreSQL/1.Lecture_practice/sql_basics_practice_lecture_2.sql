select
	f.title as "Movie Title",
	count(fa.actor_id) as "Amount of Movie Actors"
from film_actor fa 
left join actor ac using(actor_id)
left join film f using(film_id)
group by f.film_id, f.title, fa.film_id  
having  fa.film_id = 384;