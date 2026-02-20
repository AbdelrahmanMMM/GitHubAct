select * from {{source('name', 'age')}}
where id is not null