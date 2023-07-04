create table cpms(
    program varchar(255) primary key,
    activities text[],
    performance_indicator text[],
    target int[],
    accomplishment int[],
    remarks text[]
);

COPY cpms FROM '/tmp/cpms.csv'
DELIMITER ','
CSV HEADER;


create table examinees(
    no serial primary key,
    province varchar(255),
    component varchar(15) CHECK(component in ('Hands-on Exam', 'Diagnostic Exam', 'User Assessment')),
    name varchar(255),
    venue varchar(255),
    gender char(1) CHECK(gender in ('M', 'F')),
    date date,
    time char(2) CHECK(time in ('AM', 'PM')),
    status varchar(20) CHECK(status in ('Passed', 'Failed', 'For checking', 'For transmittal')),
    remarks varchar(255),
    batch varchar(255)
);


create table ojt_input(
    id serial primary key,
    province varchar(30) check (province in ('Cavite', 'Laguna', 'Batangas', 'Rizal', 'Quezon', 'RO')),
    category varchar(255) check (category in ('accepted at DICT Office', 'endorsed by partners')),
    suc varchar(255),
    duration int,
    school_address varchar(400),
    representative varchar(255),
    representative_contact varchar(15),
    student_name varchar(255),
    sex char(1) check(sex in ('M', 'F')),
    student_contact varchar(15),
    start_date date,
    end_date date, 
    mode varchar(20) check(mode in ('Physical Reporting', 'Online', 'Hybrid')),
    resume boolean,
    endorsement boolean,
    moa boolean,
    remarks varchar(10) check(remarks in ('On-going', 'Completed')) 
);