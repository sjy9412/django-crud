CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- DATA 추가(C)
-- 1. 선택적으로 추가할 때
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

-- 2. 모든 열의 데이터를 넣을 때(컬럼을 명시할 필요 없음)
INSERT INTO classmates 
VALUES (1, '홍길동', 30, '서울');

INSERT INTO classmates 
VALUES ('홍길동', 30, '서울'), ('길동', 26, '대전');

-- id값 확인하고 싶을 때 rowid로 불러옴
-- primary key 값이 있을 땐 rowid를 대체
SELECT rowid, * FROM classmates;

CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

SELECT age, name FROM classmates;

-- 원하는 column 갯수만 표시 (LIMIT)
SELECT name FROM classmates LIMIT 1;
-- 2칸 띄워서 1번째 칸 (OFFSET)
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- 해당 키워드 검색 (WHERE)
SELECT rowid, name FROM classmates WHERE address='서울';
-- 특정 column 중복 제거
SELECT DISTINCT age FROM classmates;
-- rowid를 사용하여 특정 값 삭제
-- 여러가지 값을 가진 column을 이용하여 삭제하면 모든 데이터가 사라짐
DELETE FROM classmates WHERE rowid=2;
-- AUTOINCREMENT
-- 마지막 데이터를 삭제하고 새롭게 추가해보면, id가 다시 활용되는것을 볼 수 있다.
-- 이를 방지하기 위해 AUTOINCREMENT 사용(django id값)
CREATE TABLE tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- DATA 수정(U)
UPDATE classmates SET age=25 WHERE rowid=1;
SELECT * FROM classmates;