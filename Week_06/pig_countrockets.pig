REGISTER '/home/hadoop/piggybank.jar';

dataset_with_header = LOAD '/space_missions.csv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',') AS (Company:chararray, Location:chararray, Date:chararray, Time:chararray, Rocket:chararray, Mission:chararray, RocketStatus:chararray, Price:chararray, MissionStatus:chararray);
dataset_rank = RANK dataset_with_header;
dataset_filter = FILTER dataset_rank by ($0 > 1);
dataset = foreach dataset_filter generate Company, Date, Rocket, Mission, MissionStatus;

filtered = FILTER dataset BY Company == 'NASA';
grouped = GROUP filtered BY Rocket;

counted = FOREACH grouped GENERATE group AS RocketGroup, COUNT(filtered) AS Count;

DUMP counted;
