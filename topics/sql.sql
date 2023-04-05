-- https://leetcode.com/problems/calculate-special-bonus/
SELECT
    employee_id, if(mod(employee_id, 2) <> 0 AND name NOT LIKE "M%", salary, 0) as bonus
FROM
    Employees
ORDER BY employee_id

SELECT
    employee_id, if(employee_id % 2 <> 0 AND name NOT LIKE "M%", salary, 0) as bonus
FROM
    Employees
ORDER BY employee_id

SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 <> 0 AND name NOT LIKE "M%"
        THEN salary
        ELSE 0
    END
    AS bonus
FROM
    Employees
ORDER BY employee_id

-- https://leetcode.com/problems/swap-salary/
UPDATE
    Salary
SET sex=if(sex="f", "m","f")

UPDATE
    Salary
SET sex = CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;

-- https://leetcode.com/problems/delete-duplicate-emails/
DELETE p1 FROM Person p1, Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id