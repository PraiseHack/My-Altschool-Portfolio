
CREATE SCHEMA IF NOT EXISTS ECS;


create table if not exists ECS.TESLA
(
    date timestamp primary key,
    open float not null,
    high float not null,
    low float not null,
    close float not null,
    adj_close float not null,
    volume bigint not null
);



COPY ECS.TESLA (date, open, high, low, close, adj_close, volume)
FROM '/data/tsla.csv' DELIMITER ',' CSV HEADER;