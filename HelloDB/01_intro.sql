-- 데이터베이스 생성 $ sqlite3 db.sqlite3
.databases
-- CSV 파일로 테이블 생성(.붙은건 sqlite에서만 쓰이는거고 안붙은건 sql에서 범용적으로 쓰이는 것)
.mode csv
.import helllodb.csv examples
-- 테이블 조회
SELECT * FROM examples;
-- 스키마 조회
.schema examples