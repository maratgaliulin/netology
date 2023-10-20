select 
	customer_id, rental_id, rental_date,
	row_number() over (
		partition by customer_id 
		order by rental_date desc
	) as rental_rank
from (
	select customer_id, rental_id, rental_date
	from rental r 
	where staff_id = 1 limit 500
) as sample
order by 
	customer_id,
	rental_date desc,
	rental_rank
limit 20;


select customer_id, payment_id, amount,
	amount / sum(amount) over (partition by customer_id) as strange_rating_metric	
		from (select *
			from (select customer_id, payment_id, amount,
					row_number () over(partition by customer_id order by payment_date)
					from payment p ) t
			where row_number < 4) as sample
order by customer_id, amount desc 
limit 20;


select  customer_id, payment_id, amount,
	amount - avg(amount) over(partition by customer_id) payment_deviance_simplex,
	amount - sum(amount) over(partition by customer_id) / count(amount)
over(partition by customer_id) as payment_deviance_complex
from (select * 
	from (
		select customer_id, payment_id, amount,
		row_number () over(partition by customer_id order by payment_date)
		from payment p) t
	where row_number < 4) sample
order by customer_id, amount desc 
limit 20;


select date_trunc('month', payment_date),
	lag(sum(amount), 1) over() as "Previous Payment",
	sum(amount) as "Current Payment",
	lead (sum(amount), 1) over() as "Next Payment"
from payment p 
group by date_trunc('month', payment_date); 


select 
	title, a.first_name || ' ' || a.last_name, 
	count(fa.film_id) over(partition by fa.actor_id) as amt_of_movies_acted
from film f 
join film_actor fa using (film_id)
join actor a using (actor_id) 
order by title, amt_of_movies_acted desc;



with cte_film as (
	select film_id, title,
	(case
		when length < 30 then 'Short'
		when length >= 30 and length <90 then 'Medium'
		when length >= 90 then 'Long'
	end
	) length
	from film
)
select film_id, title, length
from 
	cte_film
where 	
	length = 'Long'
order by title;


with recursive r as(
	select 1 as i,
	1 as factorial	
	union
		select 
			i+1 as i,
			factorial * (i + 1) as factorial
		from r
		where i < 10
)
select * from r;

with recursive r as(
	select 
		1 as i,
		cast(1 as bigint) as factorial
			union
				select 
					i+1 as i,
					cast((i+1) * factorial as bigint) as factorial
				from r
				where i < 20
)
select * from r;


select 
	first_name || ' ' || last_name,
	count(r.staff_id) as kj
from staff s 
join rental r using(staff_id)
group by s.staff_id;


with cte as(
	select 
		first_name || ' ' || last_name as full_name, r.rental_id, s.staff_id 
	from staff s 
	join rental r using(staff_id)
)
select full_name, count(rental_id)
from cte
group by staff_id, full_name; 



select full_name, email, title 
from(
	select 
		first_name || ' ' || last_name as full_name, email, f.title,
		row_number () over(partition by c.customer_id order by r.rental_date desc) as rn
	from customer c 
	join rental r using(customer_id)
	join inventory i on r.inventory_id = i.inventory_id 
	join film f on i.film_id = f.film_id 
	) t
where rn = 1;


create view practice_1 as
	with cte as(
		select r.*, row_number () over (partition by r.customer_id order by r.rental_date desc)
		from rental r 
	)
select c.last_name, c.email, f.title
from cte
join customer c on c.customer_id = cte.customer_id
join inventory i on i.inventory_id = cte.inventory_id
join film f on f.film_id = i.film_id 
where row_number = 1;


explain analyze
select 
	f.title, a.first_name || ' ' || a.last_name as full_name
from film f 
join film_actor fa using(film_id)
join actor a on fa.actor_id = a.actor_id 
where f.film_id < 100
order by f.title, full_name;


create table orders(
	id serial primary key,
	info json not null
);

insert into orders (info)
values
	('{"customer": "John Doe", "items": {"product": "Beer", "qty":6}}'),
	('{"customer": "Lilly Bush", "items": {"product": "Diaper", "qty":24}}'),
	('{"customer": "Nick Summers", "items": {"product": "Chainsaw", "qty":1}}'),
	('{"customer": "Alice Wonders", "items": {"product": "Magic Wand", "qty":3}}'),
	('{"customer": "Harvey Kent", "items": {"product": "Notebook", "qty":11}}');

select info from orders;

select 
	info ->'items' ->> 'product' as product,
	info ->'items' ->> 'qty' as qty
from orders o 
where info ->>'customer' = 'John Doe';


select 
	info ->> 'customer' as customer,
	info -> 'items' ->> 'qty' as qty
from orders o 
where 
	cast(info -> 'items' ->> 'qty' as integer) = 24


	
select 
	count(id) as "count"
from orders o;

select 
	sum(cast(info-> 'items' ->>'qty' as integer)) as "sum"
from orders o;

-- Возвращает значение индекса первого вхождения:
select array_position(array['a', 'b', 'c', 'd'], 'b'); 

--Возвращает длину указанной размерности массива:
select array_length(array['a', 'b', 'c', 'd'], 1);

--Содержит:
select array[1,2,4,5,3] @> array[3,1,3];

--Содержится в:
select array[2,2,7] <@ array[1,7,4,2,6];

-- Пересечение (есть общие варианты):
select array[1,4,3] && array[2,1];


select array_position(array[1,2,3,4], 3) is not null as tg; 


select * 
	from(
		select first_name || ' ' || last_name as full_name
		from actor_info ai 
		where ai.film_info like '%Animation%'
	) t1
	where full_name ilike 'liza%';


with cte2 as (
	select first_name || ' ' || last_name as full_name
	from actor_info ai 
		where ai.film_info like '%Animation%'
)
select full_name 
from cte2;


explain analyze
select * 
	from (
		select p.customer_id, p.payment_date, p.amount, row_number () over(partition by p.customer_id order by p.payment_date) as rn
		from payment p
	) Q1, payment p2 
where Q1.rn < 4;
