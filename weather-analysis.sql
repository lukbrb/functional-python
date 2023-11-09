-- SELECT 'DROP TABLE ' || name || ';' FROM sqlite_master WHERE type='table';
DROP TABLE IF EXISTS weather_data;
DROP TABLE IF EXISTS _0514;
DROP TABLE IF EXISTS _15;
DROP TABLE IF EXISTS max_0514;
DROP TABLE IF EXISTS min_0514;
DROP TABLE IF EXISTS max_15;
DROP TABLE IF EXISTS min_15;
DROP TABLE IF EXISTS max_all;
DROP TABLE IF EXISTS min_all;
DROP TABLE IF EXISTS max_record_15;
DROP TABLE IF EXISTS min_record_15;

CREATE TABLE weather_data (
    station_id TEXT,
    date DATE,
    measurement_type TEXT,
    data_value REAL
);

.separator ',' 
.import 'data/weatherdata1.csv' weather_data

ALTER TABLE weather_data ADD COLUMN Year INTEGER;
ALTER TABLE weather_data ADD COLUMN Day TEXT;

UPDATE weather_data
SET Year = CAST(strftime('%Y', Date) AS INTEGER),
    Data_Value = 0.1 * Data_Value,
    Day = strftime('%m-%d', Date);

-- Filtrer les données pour les années 2005 à 2014 (_0514)
CREATE TABLE  _0514 AS
SELECT *
FROM weather_data
WHERE Year != 2015;

-- Filtrer les données pour l'année 2015 (_15)
CREATE TABLE  _15 AS
SELECT *
FROM weather_data
WHERE Year = 2015;

-- Calculer les agrégations (max et min) pour les années 2005 à 2014 (_0514)
CREATE TABLE  max_0514 AS
SELECT Day, MAX(data_value) AS max_value
FROM _0514
GROUP BY Day;

CREATE TABLE  min_0514 AS
SELECT Day, MIN(data_value) AS min_value
FROM _0514
GROUP BY Day;

-- -- Calculer les agrégations (max et min) pour l'année 2015 (_15)
CREATE TABLE  max_15 AS
SELECT Day, MAX(Data_Value) AS max_value
FROM _15
GROUP BY Day;

CREATE TABLE  min_15 AS
SELECT Day, MIN(Data_Value) AS min_value
FROM _15
GROUP BY Day;

-- -- Fusionner les résultats pour les années 2005 à 2014 (_0514) et l'année 2015 (_15)
CREATE TABLE  max_all AS
SELECT a.Day, a.max_value AS "2005-2014", b.max_value AS "2015"
FROM max_0514 a
JOIN max_15 b
ON a.Day = b.Day;

CREATE TABLE  min_all AS
SELECT a.Day, a.min_value AS "2005-2014", b.min_value AS "2015"
FROM min_0514 a
JOIN min_15 b
ON a.Day = b.Day;

-- -- Sélectionner les enregistrements où les valeurs de 2015 sont supérieures à celles de 2005-2014
CREATE TABLE  max_record_15 AS
SELECT *
FROM max_all
WHERE "2015" > "2005-2014";

CREATE TABLE  min_record_15 AS
SELECT *
FROM min_all
WHERE "2015" < "2005-2014";

-- SELECT * FROM MAX_RECORD_15;