
create table graduates (
	rank integer,
	major_code integer,
	major varchar(200),
	total integer,
	men integer,
	women integer,
	major_category varchar(200),
	sharewomen decimal (15, 5),
	sample_size integer,
	employed integer,
	full_time integer,
	part_time integer,
	full_time_year_round integer,
	unemployed integer,
	unemployment_rate decimal (15, 5),
	median integer,
	p25th integer,
	p75th integer,
	college_jobs integer,
	non_college_jobs integer,
	low_wage_jobs integer
);

COPY graduates FROM '/tmp/graduates.csv'
DELIMITER ','
CSV HEADER;
