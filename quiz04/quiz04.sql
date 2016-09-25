
-- Locations of each cafe
create table cafes as
  select "nefeli" as name, 2 as location union
  select "brewed"        , 8             union
  select "hummingbird"   , 6;

-- Menu items at each cafe
create table menus as
  select "nefeli" as cafe, "espresso" as item union
  select "nefeli"        , "bagels"           union
  select "brewed"        , "coffee"           union
  select "brewed"        , "bagels"           union
  select "brewed"        , "muffins"          union
  select "hummingbird"   , "muffins"          union
  select "hummingbird"   , "eggs";

-- All locations on the block
create table locations as
  with locations(n) as (
    select 1 union
    select n+1 from locations where n < 10
  )
  select * from locations;

-- Locations without a cafe
create table open_locations as
  select n from locations, cafes where location != n
    group by n having count(*) == 3;

-- select * from open_locations where n >= 5;
-- Expected output:
--   5
--   7
--   9
--   10

-- Items that could be placed on a menu at an open location
create table allowed as
  with item_locations(item, location) as (
    select item, location from cafes, menus where name = cafe
  ),

  items(item) as (
    select item from menus group by item
  ),

  possible_locations_items(location, item) as (
  	select n, item from locations, items
  ),

  pen(location, item) as (
    select a.location, a.item from possible_locations_items as a, item_locations as b
                            where a.item <> b.item and abs(a.location - b.location) <= 2
  ),

  ult(location, item, num) as (
    select location, item, count(*) as num from pen group by location, item
  ),

  mate(location, maxe) as (
    select location, max(num) from ult group by location
  )

  select a.location as location, a.item as item from ult as a, mate as b where a.location = b.location and a.num = b.maxe;

-- select * from allowed where n >= 5;
-- Expected output:
--   5|bagels
--   5|coffee
--   5|espresso
--   6|espresso
--   7|espresso
--   8|espresso
--   9|eggs
--   9|espresso
--   10|eggs
--   10|espresso

-- Open locations and their maximum-length menus
create table full as
    with open_allowed(n, item) as (
        select a.location, a.item from allowed as a, open_locations as b where a.location = b.n
    ),
    
    options(location, items, last, k) as (
        select n, item, item, 1 from open_allowed union
        select n, items || ", " || item, item, k+1 from allowed, options
            where item > last and n = location
    )

    select location as n, items, max(k) from options group by location;

