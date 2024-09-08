參考

https://tsmx.net/running-oracledb-in-docker/

https://github.com/oracle/docker-images/blob/main/OracleDatabase/SingleInstance/README.md#how-to-build-and-run

https://docs.oracle.com/en/database/oracle/oracle-database/21/deeck/index.html#GUID-EDA557B2-B0D6-45E1-8FBD-C1D756803982

https://container-registry.oracle.com/ords/f?p=113:4:9235296330067:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:1863,1863,Oracle%20Database%20Free,Oracle%20Database%20Free,1,0&cs=3R3Jw46g1LsKJuqrWga8gvZsisYR2_BWE8lo66vinrvS7kd2_5RAvqjQnz_SUIkFto_ADZFC5Pn8pEZsA69NMbw


https://dev.to/docker/how-to-run-oracle-database-in-a-docker-container-using-docker-compose-1c9b

https://github.com/oracle/docker-images/issues/2362

------------


```
docker login container-registry.oracle.com

docker pull container-registry.oracle.com/database/free:latest

docker image ls | grep oracle
container-registry.oracle.com/database/free    latest    39cabc8e6db0    2 months ago    9.16GB

$ docker run --name oracle -p 1521:1521 -e ORACLE_PWD=Test123 -e ORACLE_SID=FREE -v /opt/oracle/oradata:/opt/oracle/oradata container-registry.oracle.com/database/free:latest

```

-E “ORACLE_SID”，與下面註釋的條件中使用的相同

用於某些版本的 ORACLE_SID 值：
v21.3.0 -> XE
v23.3.0 -> FREE

-----------------

test

進容器
A
bash -c "source /home/oracle/.bashrc; sqlplus /nolog"

B.
sqlplus sys/Oracle_123@//localhost:1521/free as sysdba
