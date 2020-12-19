-- 조회 : select
-- 데이터조작: insert, update, delete
-- 로그인 처리에 필요한 조회 쿼리--
SELECT
	*
FROM
	users;
	
-- select 를 수행하면 결과집합(result Set)이 나온다
-- > 모든 데이터를 가져와라

-- 조건 추가 : 제시한 uid, upw 와 일치한 회원이 있는지
-- 회원 로그인시 사용할 쿼리 확정

SELECT
	*
FROM
	users
WHERE
	uid = 'guest' AND upw = '1234';

