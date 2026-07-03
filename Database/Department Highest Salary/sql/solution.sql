select dp.name as Department, em.name as Employee, em.salary
from Employee em join Department dp 
on em.departmentId = dp.id 
where em.salary = ( select max(salary) from Employee where departmentId = dp.id )