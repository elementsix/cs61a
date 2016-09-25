create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
    select name, size from dogs, sizes where height > min and height <= max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
    select child from parents, dogs where parent = name order by height;


-- Sentences about siblings that are the same size
create table sentences as
    with siblings(s1, s2) as (
        select a.child, b.child
        from parents as a, parents as b
        where a.parent = b.parent and a.child < b.child
    ),

    siblings_of_equal_size(x1, x2, s) as (
        select s1, s2, a.size
        from siblings, size_of_dogs as a, size_of_dogs as b
        where s1 = a.name and s2 = b.name and a.size = b.size
    )

    select x1 || " and " || x2 || " are " || s || " siblings"
        from siblings_of_equal_size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
    with stack(names_of_dogs, last_dog, last_height, stack_height, stack_size) as (

        select name, name, height, height, 1 from dogs union
        select a.names_of_dogs || ", " || b.name, b.name, b.height, a.stack_height + b.height, a.stack_size + 1
            from stack as a, dogs as b
            where b.name != a.last_dog and a.stack_size < 4 and a.last_height < b.height

    )

    select names_of_dogs, stack_height
        from stack
        where stack_size = 4 and stack_height >= 170;


create table tallest as
    select height, name
        from dogs
        group by height / 10 having count(*) > 1 and height = max(height);

create table parent_child_height as
    select parent, child, a.height as parent_height, b.height as child_height
        from parents, dogs as a, dogs as b
        where parent = a.name and child = b.name;

-- All non-parent relations ordered by height difference
create table non_parents as
    with ancestors(ancestor, descendent, ancestor_height, height_diff, degrees_of_sep) as (
        select parent, child, parent_height, parent_height - child_height, 1 from parent_child_height union
        select ancestor, child, ancestor_height, ancestor_height - child_height, degrees_of_sep + 1
            from ancestors, parent_child_height where parent = descendent
    )

--    select * from ancestors where degrees_of_sep > 1;

    select ancestor, descendent, height_diff from ancestors where degrees_of_sep > 1 union
    select descendent, ancestor, -height_diff from ancestors where degrees_of_sep > 1
        order by height_diff;

