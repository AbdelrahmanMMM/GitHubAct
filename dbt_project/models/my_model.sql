select * from {{ source('source_name', 'table_name') }}
where id is not null