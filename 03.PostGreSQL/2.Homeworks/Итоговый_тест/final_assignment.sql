

--В работе использовался локальный тип подключения.

--Краткое описание БД - из каких таблиц и представлений состоит.

--БД состоит из таблиц:
--	aircrafts
--	airports
--	boarding_passes
--	bookings
--	flights
--	seats
--	ticket_flights
--	tickets

select tablename from pg_catalog.pg_tables pt 
	where schemaname = 'bookings'
order by tablename 

--Представления:
--	flights_v
	
select viewname from pg_catalog.pg_views pv 
	where schemaname = 'bookings' 

--Материализованные представления:
--	routes
	
select matviewname from pg_catalog.pg_matviews pm 
	where schemaname = 'bookings'
	
--Индексы: 
--	tickets.tickets_pkey
--	aircrafts.aircrafts_pkey
--	airports.airports_pkey
--	boarding_passes.boarding_passes_flight_id_boarding_no_key
--	boarding_passes.boarding_passes_flight_id_seat_no_key
--	boarding_passes.boarding_passes_pkey
--	bookings.bookings_pkey
--	flights.flights_flight_no_scheduled_departure_key
--	flights.flights_pkey
--	seats.seats_pkey
--	ticket_flights.ticket_flights_pkey

select tablename , indexname  from pg_catalog.pg_indexes
	where schemaname = 'bookings'

--Развернутый анализ БД - описание таблиц, логики, связей и бизнес области (частично можно взять из описания базы данных, 
--оформленной в виде анализа базы данных). Бизнес задачи, которые можно решить, используя БД.

--Основной сущностью является бронирование (bookings).
--В одно бронирование можно включить несколько пассажиров, каждому из которых
--выписывается отдельный билет (tickets). Билет имеет уникальный номер и содержит
--информацию о пассажире. Как таковой пассажир не является отдельной сущностью. Как имя,
--так и номер документа пассажира могут меняться с течением времени, так что невозможно
--однозначно найти все билеты одного человека; для простоты можно считать, что все
--пассажиры уникальны.
--Билет включает один или несколько перелетов (ticket_flights). Несколько перелетов могут
--включаться в билет в случаях, когда нет нет прямого рейса, соединяющего пункты
--отправления и назначения (полет с пересадками), либо когда билет взят «туда и обратно».
--В схеме данных нет жесткого ограничения, но предполагается, что все билеты в одном
--бронировании имеют одинаковый набор перелетов.
--Каждый рейс (flights) следует из одного аэропорта (airports) в другой. Рейсы с одним
--номером имеют одинаковые пункты вылета и назначения, но будут отличаться датой
--отправления.
--При регистрации на рейс пассажиру выдается посадочный талон (boarding_passes), в котором
--указано место в самолете. Пассажир может зарегистрироваться только на тот рейс, который
--есть у него в билете. Комбинация рейса и места в самолете должна быть уникальной, чтобы
--не допустить выдачу двух посадочных талонов на одно место.
--Количество мест (seats) в самолете и их распределение по классам обслуживания зависит
--от модели самолета (aircrafts), выполняющего рейс. Предполагается, что каждая модель
--самолета имеет только одну компоновку салона. Схема данных не контролирует, что места
--в посадочных талонах соответствуют имеющимся в самолете (такая проверка может быть
--сделана с использованием табличных триггеров или в приложении)
	
	
--Таблица bookings.aircrafts
--Каждая модель воздушного судна идентифицируется своим трехзначным кодом
--(aircraft_code). Указывается также название модели (model) и максимальная дальность полета
--в километрах (range).
	

--Таблица bookings.airports
--Аэропорт идентифицируется трехбуквенным кодом (airport_code) и имеет свое имя
--(airport_name).
--Для города не предусмотрено отдельной сущности, но название (city) указывается и может
--служить для того, чтобы определить аэропорты одного города. Также указывается широта
--(longitude), долгота (latitude) и часовой пояс (timezone).
	
	
--Таблица bookings.boarding_passes
--При регистрации на рейс, которая возможна за сутки до плановой даты отправления,
--пассажиру выдается посадочный талон. Он идентифицируется также, как и перелет —
--номером билета и номером рейса.
--Посадочным талонам присваиваются последовательные номера (boarding_no) в порядке
--регистрации пассажиров на рейс (этот номер будет уникальным только в пределах данного
--рейса). В посадочном талоне указывается номер места (seat_no).


--Таблица bookings.bookings
--Пассажир заранее (book_date, максимум за месяц до рейса) бронирует билет себе и,
--возможно, нескольким другим пассажирам. Бронирование идентифицируется номером
--(book_ref, шестизначная комбинация букв и цифр).
--Поле total_amount хранит общую стоимость включенных в бронирование перелетов всех
--пассажиров.
	
	
--Таблица bookings.flights
--Естественный ключ таблицы рейсов состоит из двух полей — номера рейса (flight_no) и даты
--отправления (scheduled_departure). Чтобы сделать внешние ключи на эту таблицу компактнее,
--в качестве первичного используется суррогатный ключ (flight_id).
--Рейс всегда соединяет две точки — аэропорты вылета (departure_airport) и прибытия
--(arrival_airport). Такое понятие, как «рейс с пересадками» отсутствует: если из одного
--аэропорта до другого нет прямого рейса, в билет просто включаются несколько необходимых
--рейсов.
--У каждого рейса есть запланированные дата и время вылета (scheduled_departure) и прибытия
--(scheduled_arrival). Реальные время вылета (actual_departure) и прибытия (actual_arrival)
--могут отличаться: обычно не сильно, но иногда и на несколько часов, если рейс задержан
	
	
--Таблица bookings.seats
--Места определяют схему салона каждой модели. Каждое место определяется своим номером
--(seat_no) и имеет закрепленный за ним класс обслуживания (fare_conditions) — Economy,
--Comfort или Business.
	
	
--Таблица bookings.ticket_flights
--Перелет соединяет билет с рейсом и идентифицируется их номерами.
--Для каждого перелета указываются его стоимость (amount) и класс обслуживания
--(fare_conditions).
	
	
--Таблица bookings.tickets
--Билет имеет уникальный номер (ticket_no), состоящий из 13 цифр.
--Билет содержит идентификатор пассажира (passenger_id) — номер документа,
--удостоверяющего личность, — его фамилию и имя (passenger_name) и контактную
--информацию (contact_date).
--Ни идентификатор пассажира, ни имя не являются постоянными (можно поменять паспорт,
--можно сменить фамилию), поэтому однозначно найти все билеты одного и того же пассажира
--невозможно.		 
	
	
--Список SQL запросов из приложения №2 с описанием логики их выполнения.
	
-- 1: В каких городах больше одного аэропорта?
	
--Делаю подзапрос, подсчитывающий, сколько раз один и тот же
--город был упомянут в таблице airports, и вывожу те города,
--которые упоминались более 1 раза
	
select *
from(
	select 
		city,
		count(city) as count_city
	from airports a
	group by city 
	) as sample
where count_city >1
order by count_city 



--2: В каких аэропортах есть рейсы, выполняемые самолетом с максимальной 
--дальностью перелета?

--Устанавливаю расширения cube, earthdistance, подсчитывающие
--расстояние по координатам, подзапросом вывожу колонки, необходимые для вычислений 
--и для читабельности информации, вычисляю расстояние в колонке distance,
--и вывожу 20 наиболее дальних рейсов
	
create extension cube;
create extension earthdistance;

select *,
point(depart_airp_long, depart_airp_lat) <@> point(arriv_airp_long, arriv_airp_lat) as distance
from(
	select  
		a.airport_name as depart_airp_name, 
		a.city as depart_airp_city, 
		a.longitude as depart_airp_long, 
		a.latitude as depart_airp_lat,
		a2.airport_name as arriv_airp_name,
		a2.city as arriv_airp_city,
		a2.longitude as arriv_airp_long,
		a2.latitude as arriv_airp_lat	
	from flights f 
	join airports a on a.airport_code = f.departure_airport 
	join airports a2 on a2.airport_code = f.arrival_airport
	group by depart_airp_name, arriv_airp_name, depart_airp_city, arriv_airp_city, depart_airp_long, depart_airp_lat, arriv_airp_long, arriv_airp_lat
	) as sample
	order by distance desc
	limit 20;

--3: Вывести 10 рейсов с максимальным временем задержки вылета

--Подзапросом вывожу необходимую для вычисления информацию, 
--вычисляю разность между запланированным и фактическим временем
--вылета самолетов, в основном запросе сортирую результаты подзапроса
--по колонке diff, и беру 10 рейсов с самым большим временем задержки

select *
from(
	select flight_id , flight_no , scheduled_departure::timestamp , actual_departure::timestamp ,
	a.airport_name || ' (' || a.city || ')' as depart_airp_name, 
		a2.airport_name || ' (' || a2.city || ')' as arriv_airp_name,
	actual_departure - scheduled_departure as diff
	from flights f 
	join airports a on a.airport_code = f.departure_airport 
	join airports a2 on a2.airport_code = f.arrival_airport
	group by flight_id , depart_airp_name, arriv_airp_name, a.city, a2.city) as sample
where diff is not null 
order by diff desc
limit 10;



--4: Были ли брони, по которым не были получены посадочные талоны?

--Получаю исходную информацию, джойню таблицы броней, билетов и
--посадочных талонов, и вывожу результаты, где посадочный номер 
--пустой (т.е. посадочный талон не был получен). Плюс решил
--попрактиковаться с мат.представлениями и индексами.

--a) без материализованного представления и без индекса:

select book_ref, 
	t.ticket_no , 
	t.passenger_name , 
	bp.boarding_no 
	from bookings b 
	left join tickets t using(book_ref)
	left join boarding_passes bp on bp.ticket_no = t.ticket_no 
	where bp.boarding_no is null
	order by t.passenger_name;

--b) с мат.представлением и индексом:

create materialized view mat_failed_bookings as	
	select book_ref, 
	t.ticket_no , 
	t.passenger_name , 
	bp.boarding_no 
	from bookings b 
	left join tickets t using(book_ref)
	left join boarding_passes bp on bp.ticket_no = t.ticket_no 
	where bp.boarding_no is null
	order by t.passenger_name;
	
create index failed_bookings_index on mat_failed_bookings
(book_ref, ticket_no, passenger_name, boarding_no);


select 
	book_ref, ticket_no, passenger_name, boarding_no 
from mat_failed_bookings;


--5: Найдите количество свободных мест для каждого рейса, их % отношение к 
--общему количеству мест в самолете. Добавьте столбец с накопительным итогом - 
--суммарное накопление количества вывезенных пассажиров из каждого аэропорта 
--на каждый день.


--Отдельными обобщенными табличными выражениями
--вычислил общее количество мест, предусмотренных самолетами,
--совершающими рейс (cte_total_seats), количество занятых мест в
--каждом рейсе (cte_occupied_seats); в главном запросе вычислил процент заполненности
--салона самолета и накопительную сумму пассажиров, вылетевших из этого аэропорта
--при помощи команды 'rows between unbounded preceding and current row'

with cte_total_seats as(
	select f.flight_id , flight_no , f.aircraft_code , f.departure_airport , f.actual_departure ,
		count(s.aircraft_code) as total_seats
	from flights f 
	join aircrafts a using(aircraft_code)
	join seats s on s.aircraft_code = a.aircraft_code 
	group by f.flight_id 
	order by f.flight_id 
	limit 5000),
----------------------------------------------------
	cte_occupied_seats as(
	select f.flight_id , flight_no , f.aircraft_code ,
		count(bp.flight_id) as occupied_seats
	from flights f 
	join aircrafts a using(aircraft_code)
	join boarding_passes bp on bp.flight_id = f.flight_id 
	group by f.flight_id 
	order by f.flight_id 
	limit 5000)
select sts.flight_id, sts.flight_no, sts.aircraft_code, sts.departure_airport, sts.actual_departure::date, sts.total_seats, sos.occupied_seats,
round((sos.occupied_seats::numeric / sts.total_seats::numeric * 100), 2) || ' %' as percent_occupied,
row_number () over(partition by sts.departure_airport, sts.actual_departure::date),
sum(sos.occupied_seats) over(partition by sts.departure_airport, sts.actual_departure::date rows between unbounded preceding and current row) as "sum"
from cte_total_seats sts
join cte_occupied_seats sos using(flight_id);


--6: Найдите процентное соотношение перелетов по типам самолетов от 
--общего количества.	

--Заджойнил таблицы самолетов и полетов по коду самолета, вывел количество перелетов
--для каждого самолета путем подсчета flight_id, соответствующих каждому самолету в
--таблице flights; процент посчитал путем деления количества полетов для каждого самолета
--на подзапрос, подсчитывающий общую сумму всех полетов
	
select 
	a.model,
	count(f.flight_id) amount_of_flights,
	round(count(f.flight_id) /
		(select 
			count(f.flight_id)
		from flights f 
		where f.actual_departure is not null
		)::dec * 100, 2) || ' %' percentage
from aircrafts a 
join flights f on f.aircraft_code = a.aircraft_code 
where f.actual_departure is not null
group by a.model;	

	
	
-- 7: Были ли города, в которые можно  добраться бизнес - классом дешевле, 
--чем эконом-классом в рамках перелета?

--Отдельным CTE вывел максимальную стоимость билета эконом-класса и минимальную стоимость
--билета бизнесс-класса для каждого рейса, и убрал ячейки Comfort. В главном запросе
--условием lag() в колонке business_min_c скопировал результат ячейки 
--cte_econ_business.business_min в вышерасположенную ячейку (со значением null) 
--для того, чтобы было удобнее сравнивать цены билетов эконом и бизнес. И вывел
--результаты с условием чтобы значение business_min_c было меньшим, чем
--значение econ_max (таких результатов не было, т.е. на всех рейсах бизнес-класс
--был дороже чем эконом)

with cte_econ_business as(
		select flight_id , fare_conditions ,
			case when fare_conditions = 'Business' then min(amount) end business_min,
			case when fare_conditions = 'Economy' then max(amount) end econ_max
	from ticket_flights tf 
	where fare_conditions = 'Business' or fare_conditions = 'Economy'
	group by flight_id , fare_conditions 
	order by flight_id , fare_conditions)
select *
from(
select flight_id , flight_no , departure_airport, cte_econ_business.econ_max,
case 
	when cte_econ_business.business_min is null then lag(cte_econ_business.business_min)over(partition by flight_id)
	when cte_econ_business.business_min is not null then cte_econ_business.business_min
end business_min_c
from flights f 
join cte_econ_business using (flight_id)
where actual_departure is not null 
group by flight_id , cte_econ_business.business_min, cte_econ_business.econ_max
order by flight_id) as sample
where business_min_c < econ_max
order by flight_id;



-- 8: Между какими городами нет прямых рейсов?

--Создал представление communicating_cities, в котором записаны все города, которые
--сообщаются между собой. В основном запросе методом декартова произведения получил
--все возможные комбинации городов, и методом except исключил из них те города,
--которые находятся в представлении (то есть те города, между которыми есть 
--сообщение)

create view communicating_cities as
	select distinct 
		a.city dep_city,
		a2.city arr_city
	from flights f 
	join airports a on f.departure_airport = a.airport_code 
	join airports a2 on f.arrival_airport = a2.airport_code;


select distinct 
	a.city depr_city,
	a2.city arrv_city 
from airports a, airports a2 
where a.city != a2.city
except 
select * from communicating_cities;



--9: Вычислите расстояние между аэропортами, связанными прямыми рейсами, 
--сравните с допустимой максимальной дальностью перелетов  в самолетах, 
--обслуживающих эти рейсы

--Заджойнил таблицы перелетов, аэропортов (2 раза - для обозначения аэропортов 
--отправления и назначения) и самолетов, вывел расстояние на которое может лететь 
--самолет из таблицы airplanes, вычислил расстояние между аэропортами по 
--формуле, округлил его, и выставил условие - если расстояние между аэропортами 
--меньше или равно расстоянию на которое может лететь самолет, то в колонке
--if_reachable будет значение Reachable, в противном случае будет выводиться 
--Unreachable.

select distinct 
	ad.airport_name origin_airport,
	aa.airport_name destination_airport,
	a."range" airplane_range,
	round((acos(sind(ad.latitude) * sind(aa.latitude) + cosd(ad.latitude) * cosd(aa.latitude) * cosd(ad.longitude - aa.longitude)) * 6371)::dec, 2) distance,		
	case when 
		a."range" <=
		acos(sind(ad.latitude) * sind(aa.latitude) + cosd(ad.latitude) * cosd(aa.latitude) * cosd(ad.longitude - aa.longitude)) * 6371 
		then 'Unreachable'
		else 'Reachable'
		end if_reachable
from flights f
join airports ad on f.departure_airport = ad.airport_code
join airports aa on f.arrival_airport = aa.airport_code
join aircrafts a on a.aircraft_code = f.aircraft_code;
