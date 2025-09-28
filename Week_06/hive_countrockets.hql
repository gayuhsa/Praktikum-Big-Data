DROP TABLE IF EXISTS test.spacemissions;

CREATE TABLE test.spacemissions (
    company STRING,
    location STRING,
    launchdate STRING,
    launchtime STRING,
    rocket STRING,
    mission STRING,
    rocketstatus STRING,
    price STRING,
    missionstatus STRING
)

ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'

WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoreChar" = "\""
)

STORED AS TEXTFILE TBLPROPERTIES('skip.header.line.count'='1');

LOAD DATA INPATH '/space_missions.csv' OVERWRITE INTO TABLE test.spacemissions;

SELECT spacemissions.rocket, COUNT(*) AS rocketcount
FROM test.spacemissions
WHERE spacemissions.company = 'NASA'
GROUP BY spacemissions.rocket;