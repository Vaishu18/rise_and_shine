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

select
  id,
  event_name,
  people_count
from
  (
    select
      *,
      count(1) over (partition by cnt) as num100
    from
      (
        select
          *,
          sum(case when people_count >= 100 then 0 else 1 end) over (
            order by
              id
          ) as cnt
        from
          event
      )
  )
where
  (num100 -1) >= 3
  and people_count >= 100
