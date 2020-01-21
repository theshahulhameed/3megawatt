
I. REST API to manage solar panel plants (CRUD operations)
---
### Usage
End-point: ```http://localhost:8000/api/plants/```

#### 1)To create a Solar Power Plant

Type: **POST** Request

Field reference:

|  Field | Type| Description | Example | Required |
| ------------- | ------------- |------------- | ------------- |------------- |
| name  | String | Name of the plant | PlantA | yes |


**Sample payload:**

```
{
"name":"planta",
}
```

**Sample response:**
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "uid": "78c479d9-1bc6-4448-9616-ca51bd8f7dd5",
    "name": "planta",
    "created_at": "2020-01-20T17:20:07.433559Z",
    "updated_at": "2020-01-20T17:20:07.433616Z"
}
```

#### 2)To list of all available solar power plants. 

End-point: ```http://localhost:8000/api/plants/```

Type: **GET** Request


**Sample response:**
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "uid": "42ee2cb4-f30b-4e4c-aa3a-93b584c4b0a7",
        "name": "planta",
        "created_at": "2020-01-18T21:29:43.600242Z",
        "updated_at": "2020-01-18T21:29:43.600787Z"
    },
    {
        "uid": "52b24270-5413-4a3b-84cd-862beee1bebf",
        "name": "planttri",
        "created_at": "2020-01-18T21:37:21.527387Z",
        "updated_at": "2020-01-18T21:37:21.527432Z"
    },
    {
        "uid": "78c479d9-1bc6-4448-9616-ca51bd8f7dd5",
        "name": "vector",
        "created_at": "2020-01-20T17:20:07.433559Z",
        "updated_at": "2020-01-20T17:20:07.433616Z"
    }
]
```

#### 3)To retrieve a particular solar power plant

Type: **GET** Request
Endpoint: `http://localhost:8000/api/plants/<uid>/`
Fields reference:

|  Field       | Type           | Description   | Example       | Required |
| ------------ | -------------- | ------------- | ------------- |------------- |
| id   | String  | UUID of the Plant | 52b24270-5413-4a3b-84cd-862beee1bebf |Yes |
 

**Sample format:**

```/api/plants/52b24270-5413-4a3b-84cd-862beee1bebf/```

**Sample response:**

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "uid": "52b24270-5413-4a3b-84cd-862beee1bebf",
    "name": "planttri",
    "created_at": "2020-01-18T21:37:21.527387Z",
    "updated_at": "2020-01-18T21:37:21.527432Z"
}
```

#### 3)To update a particular plant

Type: **PUT** Request
Endpoint: `http://localhost:8000/api/plants/<uid>/`
URL should contain valid **UID.** 

**Field reference**

|  Field | Type| Description | Example | Required |
| ------------- | ------------- |------------- | ------------- |------------- |
| name  | String | Name of the plant | PlantA | yes |


**Sample payload:**

```
{
"name":"plantx",
}
```

**Sample response:**

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "uid": "52b24270-5413-4a3b-84cd-862beee1bebf",
    "name": "plantx",
    "created_at": "2020-01-18T21:37:21.527387Z",
    "updated_at": "2020-01-20T17:34:23.056192Z"
}
```
#### 4)To delete a particular plant

Type: **DELETE** Request
Endpoint: `http://localhost:8000/api/plants/<uid>/`
URL should contain valid **UID.** 

**Sample response:**

```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```


II. REST API to pull data from monitoring service programatically
---

#### 1) To update the data for a particular solar panel plant from monitoring service for a specific time range. 

Type: **POST** Request
Endpoint: `http://localhost:8000/api/plants/<uid>/update/`
URL should contain valid **UID.** 


**Field reference**

|  Field | Type| Description | Example | Required |
| ------------- | ------------- |------------- | ------------- |------------- |
| from  | Date | A date in ISO-8601 format | 2019-02-01 | yes |
| to  | Date | A date in ISO-8601 format | 2019-02-02 | yes |


**Sample payload:**

```
{
"from":"2019-01-01T00:00:00",
"to":"2019-01-02T00:00:00"
}
```

**Sample response:**

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "uid": "52b24270-5413-4a3b-84cd-862beee1bebf",
    "name": "plantx",
    "created_at": "2020-01-18T21:37:21.527387Z",
    "updated_at": "2020-01-20T17:34:23.056192Z"
}
```


III. REST API to pull generate monitoring data reports
---

#### 1) To generate monitoring data reports for a particular solar panel plant during a time range. 

Type: **GET** Request
Endpoint: `http://localhost:8000/api/plants/<uid>/reports/`
URL should contain valid **UID.** 


**URL parameters**

|  Field | Type| Description | Example | Required |
| ------------- | ------------- |------------- | ------------- |------------- |
| month  | Integer | Takes an integer 1 (January) through 12 (December). | 1 | yes |
| year  | Integer | Takes an integer year | 2019 | yes |
| type | String | Takes either 'energy' or 'irradiation' | 'energy' | not |


**Sample request:**

```
http://localhost:8000/api/plants/52b24270-5413-4a3b-84cd-862beee1bebf/reports/?month=1&?year=2019
```

**Sample response:**

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "plant_name": "plantx",
    "readings": [
        {
            "day": "2019-01-01",
            "energy_expected": 1106.02119151029,
            "energy_observed": 1332.5873067571,
            "irradiation_observed": 951.631825587002,
            "irradiation_expected": 1389.12310900768
        },
        {
            "day": "2019-01-02",
            "energy_expected": 1070.64340229231,
            "energy_observed": 1095.13082229811,
            "irradiation_observed": 1249.070583398,
            "irradiation_expected": 1165.21219312171
        },
        {
            "day": "2019-01-03",
            "energy_expected": 1280.89440677885,
            "energy_observed": 1272.07999403483,
            "irradiation_observed": 927.647359138201,
            "irradiation_expected": 1095.35216114323
        },
        {
            "day": "2019-01-04",
            "energy_expected": 1231.84187188261,
            "energy_observed": 1187.15218519005,
            "irradiation_observed": 1000.1650636013,
            "irradiation_expected": 1191.70942870653
        },
        {
            "day": "2019-01-05",
            "energy_expected": 1128.54278647399,
            "energy_observed": 1132.54287437437,
            "irradiation_observed": 1358.72874466696,
            "irradiation_expected": 1321.78164137542
        },
        {
            "day": "2019-01-06",
            "energy_expected": 1266.90624540274,
            "energy_observed": 1345.49447803537,
            "irradiation_observed": 1457.94173804285,
            "irradiation_expected": 1247.08972205461
        },
        {
            "day": "2019-01-07",
            "energy_expected": 1356.79484045907,
            "energy_observed": 1203.42780628962,
            "irradiation_observed": 1274.46822875418,
            "irradiation_expected": 1087.33439748234
        },
        {
            "day": "2019-01-08",
            "energy_expected": 1369.45319179356,
            "energy_observed": 1175.63468379553,
            "irradiation_observed": 1022.74590940037,
            "irradiation_expected": 1184.11745539099
        },
        {
            "day": "2019-01-09",
            "energy_expected": 1076.68945167727,
            "energy_observed": 912.409343738488,
            "irradiation_observed": 962.670753187882,
            "irradiation_expected": 1103.87001712821
        },
        {
            "day": "2019-01-10",
            "energy_expected": 1079.25813438032,
            "energy_observed": 1154.21520755243,
            "irradiation_observed": 1401.70009710758,
            "irradiation_expected": 1465.98398204336
        },
        {
            "day": "2019-01-11",
            "energy_expected": 1289.92281030567,
            "energy_observed": 1370.62369095122,
            "irradiation_observed": 1278.43300651629,
            "irradiation_expected": 1052.78237011346
        },
        {
            "day": "2019-01-12",
            "energy_expected": 1338.71182272041,
            "energy_observed": 1379.54185215851,
            "irradiation_observed": 1102.56716761612,
            "irradiation_expected": 1136.46175331248
        },
        {
            "day": "2019-01-13",
            "energy_expected": 1258.256005601,
            "energy_observed": 1310.70195727335,
            "irradiation_observed": 1008.15357390629,
            "irradiation_expected": 1285.51737960893
        },
        {
            "day": "2019-01-14",
            "energy_expected": 1254.2924769365,
            "energy_observed": 1034.29601219006,
            "irradiation_observed": 1322.12749572983,
            "irradiation_expected": 1216.91418945643
        },
        {
            "day": "2019-01-15",
            "energy_expected": 1287.52156250383,
            "energy_observed": 1181.77802768203,
            "irradiation_observed": 1353.76338006108,
            "irradiation_expected": 1330.31279841982
        },
        {
            "day": "2019-01-16",
            "energy_expected": 1230.36929263981,
            "energy_observed": 1186.25375403663,
            "irradiation_observed": 1145.47304686436,
            "irradiation_expected": 1264.61520113504
        },
        {
            "day": "2019-01-17",
            "energy_expected": 1166.25748690838,
            "energy_observed": 1229.90334642644,
            "irradiation_observed": 1467.88776714863,
            "irradiation_expected": 1305.40096245661
        },
        {
            "day": "2019-01-18",
            "energy_expected": 1256.24866849329,
            "energy_observed": 1245.22694953676,
            "irradiation_observed": 1353.36511756096,
            "irradiation_expected": 1245.77167518873
        },
        {
            "day": "2019-01-19",
            "energy_expected": 1138.42973209781,
            "energy_observed": 1206.86643070731,
            "irradiation_observed": 1111.04204580423,
            "irradiation_expected": 1319.47430088955
        },
        {
            "day": "2019-01-20",
            "energy_expected": 1494.00815261076,
            "energy_observed": 1017.31360227586,
            "irradiation_observed": 984.023340973156,
            "irradiation_expected": 1340.77896120244
        },
        {
            "day": "2019-01-21",
            "energy_expected": 1303.79240464944,
            "energy_observed": 785.385035234484,
            "irradiation_observed": 1024.14112010893,
            "irradiation_expected": 1245.53245962332
        },
        {
            "day": "2019-01-22",
            "energy_expected": 1026.46874099089,
            "energy_observed": 1241.97324450027,
            "irradiation_observed": 1341.76698183752,
            "irradiation_expected": 1224.40979097798
        },
        {
            "day": "2019-01-23",
            "energy_expected": 1231.57073353254,
            "energy_observed": 844.206707424551,
            "irradiation_observed": 1283.18383692911,
            "irradiation_expected": 1108.26781752704
        },
        {
            "day": "2019-01-24",
            "energy_expected": 1214.09978070328,
            "energy_observed": 1300.04430204905,
            "irradiation_observed": 1243.1663006778,
            "irradiation_expected": 848.502497090001
        },
        {
            "day": "2019-01-25",
            "energy_expected": 1333.6811017309,
            "energy_observed": 1250.32545212521,
            "irradiation_observed": 1233.19676907582,
            "irradiation_expected": 893.254553363461
        },
        {
            "day": "2019-01-26",
            "energy_expected": 1419.27990918716,
            "energy_observed": 1266.03703104687,
            "irradiation_observed": 1263.36180613509,
            "irradiation_expected": 1082.48299835092
        },
        {
            "day": "2019-01-27",
            "energy_expected": 1425.24523198261,
            "energy_observed": 1358.15883303868,
            "irradiation_observed": 1337.40134875602,
            "irradiation_expected": 1194.37503968792
        },
        {
            "day": "2019-01-28",
            "energy_expected": 1441.16121781462,
            "energy_observed": 1291.06612074245,
            "irradiation_observed": 1314.71121177673,
            "irradiation_expected": 1243.60352316001
        },
        {
            "day": "2019-01-29",
            "energy_expected": 1417.46834760071,
            "energy_observed": 994.489976852182,
            "irradiation_observed": 1110.08857486593,
            "irradiation_expected": 1333.42768452656
        },
        {
            "day": "2019-01-30",
            "energy_expected": 1409.77087923748,
            "energy_observed": 1170.38261614935,
            "irradiation_observed": 1216.05619836115,
            "irradiation_expected": 1196.49866679846
        },
        {
            "day": "2019-01-31",
            "energy_expected": 1236.62779813359,
            "energy_observed": 1203.74352258985,
            "irradiation_observed": 941.858288275895,
            "irradiation_expected": 1374.58859384954
        }
    ]
}
```







