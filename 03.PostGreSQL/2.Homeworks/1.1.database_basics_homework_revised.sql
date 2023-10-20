--������� 1. �������� ���������� �������� ������� �� ������� �������.
select
	distinct city
from
	city c;
--������� 2. ����������� ������ �� ����������� �������, ����� ������ ������� ������ �� ������, �������� ������� ���������� �� �L� � ������������� �� �a�, � �������� �� �������� ��������.
select
	distinct city
from
	city c2
where
	city like 'L%a'
	and city not like '% %';
--������� 3. �������� �� ������� �������� �� ������ ������� ���������� �� 
--��������, ������� ����������� � ���������� � 17 ���� 2005 ���� �� 19 ���� 2005 ���� 
--������������ � ��������� ������� ��������� 1.00. ������� ����� ������������� �� ���� �������.
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
--������� 4. �������� ���������� � 10-�� ��������� �������� �� ������ �������.
select
	payment_id,
	payment_date,
	amount
from
	payment p
order by
	payment_date desc
limit 10;
--������� 5. �������� ��������� ���������� �� �����������:
select
	concat(last_name , ' ', first_name) as "������� � ���",
	email as "����������� �����",
	character_length(email) as "����� email",
	date(last_update) as "����"
from
	customer c;
--�������� ����� �������� ������ �������� �����������, ����� ������� KELLY ��� WILLIE. ��� ����� � ������� � ����� �� �������� �������� ������ ���� ���������� � ������ �������.
select
	lower(last_name) ,
	lower(first_name) ,
	active
from
	customer c
where
	activebool and
	(first_name in ('KELLY', 'WILLIE'));
-- �������������� �����
--������� 1.�������� ����� �������� ���������� � �������, � ������� ������� �R� � 
--��������� ������ ������� �� 0.00 �� 3.00 ������������, � ����� ������ c ��������� �PG-13� 
--� ���������� ������ ������ ��� ������ 4.00.
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
--�������� ���������� � ��� ������� � ����� ������� ��������� ������.
select
	film_id,
	title,
	description
from
	film f
order by
	LENGTH(description) desc
limit 3;
--�������� Email ������� ����������, �������� �������� Email �� 2 ��������� �������:
select
	customer_id,
	email,
	split_part(email, '@', 1) as "Email before @",
	split_part(email, '@', 2) as "Email after @"
from
	customer c;
--������� 4. ����������� ������ �� ����������� �������, �������������� �������� � ����� ��������: ������ ����� ������ ���� ���������, ��������� ���������.

select 
	customer_id,
	email, 
	upper(left(email, 1))|| lower(right(split_part(email, '@', 1), -1))  as "Email before @",
	upper(left(split_part(email, '@', 2), 1))|| lower(right(split_part(email, '@', 2), -1))  as "Email after @"
from
	customer c ;
