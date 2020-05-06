with result as (
select
  *,
  row_number() over(partition by cnt) pnt
from
  (
    select
      E.*,
      (case when people_count >= 10 then 1 else 0 end) as cnt
    from
      event E
  ) t1
  )
select result.* from result where result.pnt>=2 and result.cnt!=0
