-- CREATE TABLE event ( id INTEGER PRIMARY KEY AUTOINCREMENT, event_name VARCHAR(20), people_count INTEGER )
-- insert into event values
-- (1, 'A', 10),
-- (2, 'B', 20),
-- (3, 'C', 100),
-- (4, 'F', 150),
-- (5, 'G', 900),
-- (6, 'HH', 300),
-- (7, 'CJ', 100),
-- (8, 'FQ', 50),
-- (9, 'GF', 900),
-- (10, 'HE', 300),
-- (11, 'GFF', 400),
-- (12, 'HQE', 300);

with result as (
select
  *,
  row_number() over(partition by cnt) pnt
from
  (
    select
      E.*,
      (case when people_count >= 100 then 1 else 0 end) as cnt
    from
      event E
  ) t1
  )
select result.* from result where result.pnt>=3 and result.cnt!=0
