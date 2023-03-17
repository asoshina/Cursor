USE task5;
--Таблиця Employees. Отримати список з інформацією про всіх співробітників
SELECT * FROM employees;
--Таблиця Employees. Отримати список всіх співробітників з ім'ям 'David'
SELECT * FROM employees WHERE first_name='David';
--Таблиця Employees. Отримати список всіх співробітників з 20го і з 30го відділу (department_id)
SELECT * FROM employees WHERE department_id in (20,30);
--Таблиця Employees. Отримати список всіх співробітників з 50го і з 80го відділу (department_id) у яких є бонус (значення в колонці commission_pct не порожнє)
SELECT * FROM employees WHERE department_id in (10,80) and commission_pct is not null;
--Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в перший день місяця (будь-якого)
SELECT * FROM employees WHERE DAY(hire_date)=1;
--Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в 2008ом році
SELECT * FROM employees WHERE YEAR(hire_date)=2008;
--Таблиця DUAL. Показати завтрашню дату в форматі: Tomorrow is Second day of January
SELECT DATE_FORMAT(DATE_ADD(CURRENT_DATE(), INTERVAL 1 DAY), 'Tomorrow is %D day of %M');
--Таблиця Employees. Отримати список всіх співробітників і дату приходу на роботу кожного в форматі: 21st of June, 2007
SELECT first_name, last_name, DATE_FORMAT(hire_date,'%D of %M, %Y') as hire_data FROM employees;
--Таблиця Employees. Отримати список працівників зі збільшеними зарплатами на 20%. Зарплату показати зі знаком долара
SELECT first_name, last_name, CONCAT(salary,' $') as salary, CONCAT(commission_pct, '%') as commission FROM employees WHERE commission_pct=20;
--Таблиця Employees. Отримати список всіх     співробітників які пришили на роботу в лютому 2007го року.
SELECT first_name, last_name, hire_date FROM employees WHERE MONTH(hire_date)=2 and YEAR(hire_date)=2007;
--Таблиця DUAL. Вивезти актуальну дату, + секунда, + хвилина, + годину, + день, + місяць, + рік
SELECT NOW(),DATE_ADD(DATE_ADD(DATE_ADD(NOW(), INTERVAL '1 1:1:1' DAY_SECOND), INTERVAL 1 MONTH), INTERVAL 1 YEAR)
--Таблиця Employees. Отримати список всіх співробітників з повними зарплатами (salary + commission_pct (%)) в форматі: $ 24,000.00
SELECT first_name, last_name, CONCAT('$ ', FORMAT(salary+salary*commission_pct/100,2)) as full_salary FROM employees;
--Таблиця Employees. Отримати список всіх співробітників і інформацію про наявність бонусів до зарплати (Yes / No)
SELECT first_name, last_name, (
	CASE
		WHEN commission_pct is not NULL THEN 'YES'
		WHEN commission_pct is NULL THEN 'NO'
       END ) as commission from employees;