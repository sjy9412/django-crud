-- DDK(데이터 정의 언어)
-- 관계형 데이터 베이스 구조를 정의하기 위한 명령어
-- CREATE DROP ALTER
-- 테이블 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- 테이블 목록 조회
.tables

-- 테이블 스키마 조회
.schema classmates

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블 변경
-- 새로운 COLUMN을 추가해주려면 디폴트 값을 설정해줘야함
ALTER TABLE articles RENAME TO news

-- 스키마 변경
-- 기존 테이블
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
-- 1. 기존 테이블명 tmp 변경
ALTER TABLE friends RENAME TO tmp;
-- 2. 새롭게 테이블 만들고
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location VARCHAR(100) NOT NULL
);
-- 3. 데이터 이동
INSERT INTO friends SELECT * FROM tmp;
-- 4. tmp 테이블 삭제
DROP TABLE tmp;