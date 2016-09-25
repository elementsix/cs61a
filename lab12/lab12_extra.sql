-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table alphabetical_paths as
  with
    paths(s, n, last) as (
      -- REPLACE THIS LINE
      select s1, 1, s1 from adjacencies union
      select s || "," || s2, n + 1, s2 from paths, adjacencies where last = s1 and last < s2
    )
  select s from paths where n > 6 order by -n;

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      -- REPLACE THIS LINE
      select s1, s2, 1 from adjacencies, landlocked where s2 = state union
      select start, s2, hops + 1 from inland, adjacencies, landlocked
            where end = s1 and s2 = state and hops < 10
    )
  -- REPLACE THIS LINE
  select * from inland;
