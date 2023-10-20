--������� 1. �������� ��� ������� ���������� ��� �����, ����� � ������ ����������.

select 
	concat(last_name, ' ', first_name) as "Customer name",
	a.address,
	c2.city,
	cou.country 
from customer c 
full outer join address a on c.address_id = a.address_id 
full outer join city c2 on c2.city_id = a.city_id 
full outer join country cou on cou.country_id = c2.country_id;


--������� � ������� ��������� ����� USING:

select 
	concat(last_name, ' ', first_name) as "Customer name",
	a.address,
	c2.city,
	cou.country 
from customer c 
full outer join address a using(address_id)
full outer join city c2 using(city_id)
full outer join country cou using(country_id)


--������� 2. � ������� SQL-������� ���������� ��� ������� �������� ���������� ��� �����������.

select 
	s.store_id as "ID ��������",
	count (c.store_id) as "���������� �����������"
from store s 
full outer join customer c on c.store_id = s.store_id
group by s.store_id;


--������� 2.1 - ������������� ������� � ����������� ����������� > 300

select 
	s.store_id as "ID ��������",
	count (c.store_id) as "���������� �����������"
from store s 
full outer join customer c using(store_id)
group by s.store_id 
having count (c.store_id) > 300;

-- ������� 2.2 - ����������� ������, ������� � ���� ���������� � ������ 
--��������, ������� � ����� ��������, ������� �������� � ��.

select 
	s.store_id as "ID ��������",
	count (c.store_id) as "���������� �����������",
	cty.city as "�����",
	concat(s2.last_name, ' ', s2.first_name) as "��� ����������" 
from store s 
left join address a using(address_id) 
left join staff s2 on s2.staff_id = s.manager_staff_id 
left join city cty using(city_id)
left join customer c on c.store_id = s.store_id
group by s.store_id, cty.city_id, s2.last_name, s2.first_name
having count (c.store_id) > 300;


--ВАРИАНТ УЧИТЕЛЯ

select 
	*
from (
	select
		store_id as "ID ��������",
		count (customer_id) as "���������� �����������"
	from customer c
	group by store_id
	having count (customer_id) > 300
) t
--join store s on s.store_id = t.store_id
--join address a on a.address_id = t.address_id 
--join city c2 on c2.city_id = a.city_id 
--join staff s2 on s2.staff_id = s.manager_staff_id 




--������� 3. �������� ���-5 �����������, ������� ����� � ������ �� �� ����� ���������� ���������� �������.

select 
	concat(last_name, ' ', first_name) as "������� � ��� ����������",
	count(p.customer_id) as "���������� �������" 
from customer c 
left join payment p on p.customer_id = c.customer_id 
group by c.customer_id
order by "���������� �������" desc limit 5;


--������� 4. ���������� ��� ������� ���������� 4 ������������� ����������:
--	���������� ������ � ������ �������;
--	����� ��������� �������� �� ������ ���� ������� (�������� ��������� �� ������ �����);
--	����������� �������� ������� �� ������ ������;
--	������������ �������� ������� �� ������ ������.
 

select 
	concat(last_name, ' ', first_name) as "������� � ��� ����������",
	count(p.customer_id) as "���������� �������",
	round(sum(p.amount), 0)  as "����� ��������� ��������",
	min(p.amount) as "����������� ��������� �������",
	max(p.amount) as "������������ ��������� �������" 
from customer c 
left join payment p on p.customer_id = c.customer_id 
group by c.customer_id
order by "������� � ��� ����������" asc;


--������� 5. ��������� ������ �� ������� �������, ��������� ����� �������� ������������ 
--���� ������� ���, ����� � ���������� �� ���� ��� � ����������� ���������� �������. 
--��� ������� ���������� ������������ ��������� ������������.


select 
	c.city as "����� 1", 
	c1.city as "����� 2"
from city c 
cross join city c1 where c.city != c1.city;


--������� 6. ��������� ������ �� ������� rental � ���� ������ ������ � ������ 
--(���� rental_date) � ���� �������� (���� return_date), ��������� ��� ������� 
--���������� ������� ���������� ����, �� ������� �� ���������� ������.


select 
	customer_id as "ID ����������",
	round(cast((sum(date_part('day', return_date - rental_date) + date_part('hour', return_date - rental_date)/24))/count(customer_id) as numeric), 2) as "������� ���������� ���� �� �������"
from rental r 
group by customer_id 
order by customer_id;


--�������������� �������:


--������� 1. ���������� ��� ������� ������, ������� ��� ��� ����� � ������, 
--� ����� ����� ��������� ������ ������ �� �� �����.

select 
	title as "�������� ������",	 
	rating as "�������",
	c."name" as "����",
	release_year as "��� �������",
	l."name" as "����",
	count(r.inventory_id) as "���������� �����",
	sum(p.amount) as "����� ��������� ������"
from film f 
left join film_category fc using(film_id)
left join category c on fc.category_id = c.category_id 
left join "language" l using(language_id) 
left join inventory i using(film_id)
left join rental r on r.inventory_id = i.inventory_id 
left join payment p on p.rental_id = r.rental_id 
group by f.film_id, title, c."name", l."name" 
order by title;

--������� 2. ����������� ������ �� ����������� ������� � �������� 
--� ������� ���� ������, ������� �� ���� �� ����� � ������.

select 
	title as "�������� ������",	 
	rating as "�������",
	c."name" as "����",
	release_year as "��� �������",
	l."name" as "����",
	count(r.inventory_id) as "���������� �����",
	sum(p.amount) as "����� ��������� ������"
from film f 
left join film_category fc using(film_id)
left join category c on fc.category_id = c.category_id 
left join "language" l using(language_id) 
left join inventory i using(film_id)
left join rental r on r.inventory_id = i.inventory_id 
left join payment p on p.rental_id = r.rental_id 
group by f.film_id, title, c."name", l."name" 
having count(r.inventory_id) = 0
order by title;


--������� 3. ���������� ���������� ������, ����������� ������ ���������. 
--�������� ����������� ������� ��������. ���� ���������� ������ ��������� 
--7 300, �� �������� � ������� ����� ���, ����� ������ ���� �������� ����.

select 
	staff_id,
	count(p.staff_id),
	case when count(p.staff_id) > 7300 then '��'
		else '���'
		end as "������"
from staff s 
left join payment p using(staff_id)
group by s.staff_id 