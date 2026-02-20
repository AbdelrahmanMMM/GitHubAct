select * from {{ source('source_name', 'table_name') }}
where age is not null