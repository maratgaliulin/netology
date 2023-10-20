--=============== МОДУЛЬ 5. РАБОТА С POSTGRESQL =======================================




--ЗДРАВСТВУЙТЕ! ПРОШУ ПРОЩЕНИЯ ЧТО ЗАДЕРЖАЛ ВЫПОЛНЕНИЕ ДОМАШНЕГО ЗАДАНИЯ: ОЧЕНЬ МНОГО НАВАЛИЛОСЬ РАБОТЫ, Т.К. СЕЙЧАС ОТПУСКНОЙ ПЕРИОД,
--И ВСЕ КТО НА РАБОТЕ, ВЫНУЖДЕНЫ БРАТЬ НА СЕБЯ ДОПОЛНИТЕЛЬНУЮ НАГРУЗКУ (СВЕРХУРОЧНАЯ РАБОТА В ОТДЕЛЕНИИ + ДОПОЛНИТЕЛЬНЫЕ ДЕЖУРСТВА).
--Я ПОСТАРАЛСЯ ПОСМОТРЕТЬ ВСЕ ВИДЕОЛЕКЦИИ, НЕ УСПЕЛ ЛИШЬ ПОСМОТРЕТЬ ВЕБИНАР С РАЗБОРОМ ДОМАШНЕГО ЗАДАНИЯ. ПОЭТОМУ ПРИШЛОСЬ СДЕЛАТЬ ТАК,
--В КАКОЙ МЕРЕ Я ПОНЯЛ ДАННУЮ ТЕМУ (А ТЕМА ОКАЗАЛАСЬ НЕ ИЗ ПРОСТЫХ, ДОЛЖЕН ПРИЗНАТЬ - ПРИХОДИЛОСЬ ПЕРЕСМАТРИВАТЬ КАЖДОЕ ВИДЕО ПО НЕСКОЛЬКО РАЗ,
--ЧТОБЫ РАЗОБРАТЬСЯ)). ПОЭТОМУ ПРОШУ ПРОЩЕНИЯ ЗА ВЕРОЯТНЫЕ ОШИБКИ, КОТОРЫЕ ЕСТЬ В ДЗ. ОБЕЩАЮ ВЫПОЛНИТЬ ТАКЖЕ И ДОП.ЗАДАНИЕ, ТЕМЫ ИНТЕРЕСНЫЕ И
--МНЕ САМОМУ ХОЧЕТСЯ ЗАКРЕПИТЬ ПОЛУЧЕННЫЕ ЗНАНИЯ, ПРОСТО ВРЕМЕНИ К СОЖАЛЕНИЮ НЕ ВСЕГДА ХВАТАЕТ :( 





--ЗАДАНИЕ №1
--Сделайте запрос к таблице payment и с помощью оконных функций добавьте вычисляемые колонки согласно условиям:

--Пронумеруйте все платежи от 1 до N по дате

select payment_id, amount, payment_date
from(
	select payment_id, amount, payment_date, row_number () over(order by payment_date asc) as rn
	from payment p
) t;


--Пронумеруйте платежи для каждого покупателя, сортировка платежей должна быть по дате

select payment_id, amount, payment_date, customer_id, c.first_name || ' ' || c.last_name,
	row_number () over(partition by customer_id order by payment_date asc) as rn
from payment p
join customer c using(customer_id)

--Посчитайте нарастающим итогом сумму всех платежей для каждого покупателя, сортировка должна 
--быть сперва по дате платежа, а затем по сумме платежа от наименьшей к большей

--1)Сортировка по дате платежа:

select customer_id, c.first_name || ' ' || c.last_name as full_name, payment_id, payment_date, amount, 
	row_number () over(partition by customer_id order by payment_date asc) as customer_paym_number,
	row_number () over(order by payment_date asc) as total_paym_number,
	sum(amount) over(partition by customer_id order by payment_date asc rows between unbounded preceding and current row) as "sum"
from payment p
join customer c using(customer_id)
group by payment_id, customer_id;

--2) Сортировка по сумме платежа:

select customer_id, c.first_name || ' ' || c.last_name as full_name, payment_id, payment_date, amount, 
	row_number () over(partition by customer_id order by amount asc) as customer_paym_number,
	row_number () over(order by amount asc) as total_paym_number,
	dense_rank () over(partition by customer_id order by amount asc) as ascend_amnt_payment,
	sum(amount) over(partition by customer_id order by amount asc rows between unbounded preceding and current row) as "sum"
from payment p
join customer c using(customer_id)
group by payment_id, customer_id;

--Пронумеруйте платежи для каждого покупателя по стоимости платежа от наибольших к меньшим 
--так, чтобы платежи с одинаковым значением имели одинаковое значение номера.
--Можно составить на каждый пункт отдельный SQL-запрос, а можно объединить все колонки в одном запросе.

select customer_id, c.first_name || ' ' || c.last_name as full_name, payment_id, payment_date, amount, 
	row_number () over(partition by customer_id order by payment_date asc) as customer_paym_number,
	row_number () over(order by payment_date asc) as total_paym_number,
	dense_rank () over(partition by customer_id order by amount asc) as ascend_amnt_payment,
	sum(amount) over(partition by customer_id order by payment_date asc rows between unbounded preceding and current row) as "sum"
from payment p
join customer c using(customer_id)
group by payment_id, customer_id;


--ЗАДАНИЕ №2
--С помощью оконной функции выведите для каждого покупателя стоимость платежа и стоимость 
--платежа из предыдущей строки со значением по умолчанию 0.0 с сортировкой по дате.


select customer_id, c.first_name || ' ' || c.last_name as full_name, payment_id, payment_date, amount, 
	(case 
		when lag (amount, 1) over(partition by customer_id order by payment_date asc) is null then 0.00
		when lag (amount, 1) over(partition by customer_id order by payment_date asc) is not null then lag (amount, 1) over(partition by customer_id order by payment_date asc)
	end 
	) as previous_amount
from payment p
join customer c using(customer_id)
group by payment_id, customer_id;


--ЗАДАНИЕ №3
--С помощью оконной функции определите, на сколько каждый следующий платеж покупателя больше или меньше текущего.

select customer_id, c.first_name || ' ' || c.last_name as full_name, payment_id, payment_date, amount, 
 	amount - lead (amount, 1) over(partition by customer_id order by payment_date asc) as difference
from payment p
join customer c using(customer_id)
group by payment_id, customer_id;


--ЗАДАНИЕ №4
--С помощью оконной функции для каждого покупателя выведите данные о его последней оплате аренды.

select 	c.first_name || ' ' || c.last_name as full_name, customer_id, payment_id, amount, payment_date
	from(
		select *
			from(
				select customer_id, payment_id, payment_date, amount,
					row_number () over(partition by customer_id order by payment_date desc) "num"
					from payment p 
			) select_for_limit
			where "num" = 1
	) t
	join customer c using(customer_id)
	order by customer_id asc;


--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--С помощью оконной функции выведите для каждого сотрудника сумму продаж за август 2005 года 
--с нарастающим итогом по каждому сотруднику и по каждой дате продажи (без учёта времени) 
--с сортировкой по дате.

select *, 
	sum("sum") over(partition by staff_id order by pd asc rows between unbounded preceding and current row) as "sum_total"
from(select full_name, staff_id, sum(amount) as "sum", pd 
	 from (
		select s.first_name || ' ' || s.last_name as full_name, staff_id, amount, date_trunc('day', payment_date)::date as pd
		from payment p
		join staff s using(staff_id)
	 ) t
where pd >= '2005-08-01 00:00:00.000' and pd <= '2005-08-31 00:00:00.000'
group by pd, full_name, staff_id
)k
order by staff_id, pd;


--ЗАДАНИЕ №2
--20 августа 2005 года в магазинах проходила акция: покупатель каждого сотого платежа получал
--дополнительную скидку на следующую аренду. С помощью оконной функции выведите всех покупателей,
--которые в день проведения акции получили скидку

with cte as (select customer_id, payment_date
from payment p 
where payment_date >= '2005-08-20 00:00:00.000' and payment_date <= '2005-08-20 23:59:59.999'
order by payment_date asc)
select *
from(
	select *,
		row_number () over(order by payment_date asc) as rn
	from cte) as smpl
where rn % 100 = 0;


--ЗАДАНИЕ №3
--Для каждой страны определите и выведите одним SQL-запросом покупателей, которые попадают под условия:
-- 1. покупатель, арендовавший наибольшее количество фильмов
-- 2. покупатель, арендовавший фильмов на самую большую сумму
-- 3. покупатель, который последним арендовал фильм

with cte1 as(
	select country, full_name as "Покупатель, арендовавший на самую большую сумму"
	from(
		select *, row_number ()over(partition by country order by total_payment desc) as rn
		from(
			select c.country as "country", first_name || ' ' || last_name as full_name,
			sum(amount) as "total_payment"
			from payment
		join customer cst using (customer_id)
		join address a on a.address_id = cst.address_id 
		join city ct on ct.city_id = a.city_id 
		join country c on c.country_id = ct.country_id 
		group by c.country, customer_id
		order by c.country) t
	)p 
where rn = 1),
cte2 as(
	select country, full_name as "Покупатель, арендовавший наибольшее кол-во фильмов"
	from(
		select *, row_number ()over(partition by country order by total_amnt_of_movies desc) as rn
		from(
		select c.country as "country", first_name || ' ' || last_name as full_name,
			count(customer_id) as "total_amnt_of_movies"
			from payment
		join customer cst using (customer_id)
		join address a on a.address_id = cst.address_id 
		join city ct on ct.city_id = a.city_id 
		join country c on c.country_id = ct.country_id 
		group by c.country, customer_id
		order by c.country) t
)p 
where rn = 1),
cte3 as(
	select country, full_name as "Покупатель, арендовавший фильм последним"
	from(
		select *, row_number ()over(partition by country order by payment_date desc) as rn
		from(
			select c.country as "country", first_name || ' ' || last_name as full_name,
			payment_date
			from payment
		join customer cst using (customer_id)
		join address a on a.address_id = cst.address_id 
		join city ct on ct.city_id = a.city_id 
		join country c on c.country_id = ct.country_id 
		group by c.country, customer_id, payment_date
		order by c.country) t
)p 
where rn = 1)
select cte1.country, "Покупатель, арендовавший наибольшее кол-во фильмов", 
	"Покупатель, арендовавший на самую большую сумму", 
	"Покупатель, арендовавший фильм последним"
from cte2
join cte1 using(country)
join cte3 using(country);


