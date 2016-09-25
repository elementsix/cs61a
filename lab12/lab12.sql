-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table california as
  -- REPLACE THIS LINE
  select s1, s2 from adjacencies where s1 == 'CA';

-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
      -- REPLACE THIS LINE
      select s1, s2, 1 from adjacencies union
      select a.start, b.s2, a.hops + 1 from distance as a, adjacencies as b where a.end = b.s1 and a.hops < 15
    )
  select * from distance;

create table three_hops as
  -- REPLACE THIS LINE
   with
    distance(start, end, hops) as (
      -- REPLACE THIS LINE
      select s1, s2, 1 from adjacencies union
      select a.start, b.s2, a.hops + 1 from distance as a, adjacencies as b where a.end = b.s1 and a.hops < 15
    )
   select end from distance where start = 'CA' and hops == 3;
