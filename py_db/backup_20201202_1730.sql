-- 스톡 목록 가져오기(조회)
SELECT NAME FROM stock;
-- 스톡 목록 가져오기(조회) 5개만
SELECT NAME FROM stock LIMIT 5;
-- 스톡 목록 가져오기(조회) 5개만, 2번째 페이지부터
SELECT NAME FROM stock LIMIT 5, 5;
-- limit (페이지번호-1)*(페이지당데이터개수),(페이지당데이터개수)
SELECT NAME FROM stock LIMIT 10, 5;
-- 정렬하기 : order by 컬럼명 (asc or desc)
SELECT NAME FROM stock ORDER BY NAME DESC;
SELECT NAME FROM stock ORDER BY NAME ASC;
-- 이름 기준 오름 차순으로 정렬하여 상이 python_dbstockstock2stock상위 5개를 가져와라
SELECT NAME FROM stock ORDER BY NAME ASC LIMIT 0, 5;
