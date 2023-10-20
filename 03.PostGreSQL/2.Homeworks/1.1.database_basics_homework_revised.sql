--Задание 1. Выведите уникальные названия городов из таблицы городов.
select
	distinct city
from
	city c;
--Задание 2. Доработайте запрос из предыдущего задания, чтобы запрос выводил только те города, названия которых начинаются на “L” и заканчиваются на “a”, и названия не содержат пробелов.
select
	distinct city
from
	city c2
where
	city like 'L%a'
	and city not like '% %';
--Задание 3. Получите из таблицы платежей за прокат фильмов информацию по 
--платежам, которые выполнялись в промежуток с 17 июня 2005 года по 19 июня 2005 года 
--включительно и стоимость которых превышает 1.00. Платежи нужно отсортировать по дате платежа.
select
	payment_id,
	payment_date,
	amount
from
	payment p
where
	payment_date::date between '2005-06-15' and '2005-06-17'
	and amount > 1.0
order by
	payment_date;
--Задание 4. Выведите информацию о 10-ти последних платежах за прокат фильмов.
select
	payment_id,
	payment_date,
	amount
from
	payment p
order by
	payment_date desc
limit 10;
--Задание 5. Выведите следующую информацию по покупателям:
select
	concat(last_name , ' ', first_name) as "Фамилия и имя",
	email as "Электронная почта",
	character_length(email) as "Длина email",
	date(last_update) as "Дата"
from
	customer c;
--Выведите одним запросом только активных покупателей, имена которых KELLY или WILLIE. Все буквы в фамилии и имени из верхнего регистра должны быть переведены в нижний регистр.
select
	lower(last_name) ,
	lower(first_name) ,
	active
from
	customer c
where
	activebool and
	(first_name in ('KELLY', 'WILLIE'));
-- Дополнительная часть
--Задание 1.Выведите одним запросом информацию о фильмах, у которых рейтинг “R” и 
--стоимость аренды указана от 0.00 до 3.00 включительно, а также фильмы c рейтингом “PG-13” 
--и стоимостью аренды больше или равной 4.00.
select
	title,
	description,
	rating,
	rental_rate
from
	film f
where
	rating = 'R'
	and rental_rate <= 3.00
	or rating = 'PG-13'
	and rental_rate >= 4.00
order by
	rating;
--Получите информацию о трёх фильмах с самым длинным описанием фильма.
select
	film_id,
	title,
	description
from
	film f
order by
	LENGTH(description) desc
limit 3;
--Выведите Email каждого покупателя, разделив значение Email на 2 отдельных колонки:
select
	customer_id,
	email,
	split_part(email, '@', 1) as "Email before @",
	split_part(email, '@', 2) as "Email after @"
from
	customer c;
--Задание 4. Доработайте запрос из предыдущего задания, скорректируйте значения в новых колонках: первая буква должна быть заглавной, остальные строчными.

select 
	customer_id,
	email, 
	upper(left(email, 1))|| lower(right(split_part(email, '@', 1), -1))  as "Email before @",
	upper(left(split_part(email, '@', 2), 1))|| lower(right(split_part(email, '@', 2), -1))  as "Email after @"
from
	customer c ;
