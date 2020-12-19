-- *를 쓰는 것은 부하가 걸려서 적절치 않으나, 일단 편의상사용
SELECT * FROM stocks ORDER BY NAME ASC LIMIT 0,5;

-- 동일 종목끼리만 보여줘라 -> indu -> 주식에서 sector
SELECT * FROM stocks WHERE indu='기타 금융업';


-- 검색어를 이용하여 검색
-- 삼성이라는 단어만 들어있으면 된다 % 삼성%
SELECT * FROM stocks WHERE NAME like '%삼성% ';
