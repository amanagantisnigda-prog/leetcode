# Write your MySQL query statement below
UPDATE Salary set sex= case when sex='m' THEN 'f' when sex='f' then 'm' 
END;