-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

--SELECT b.title, m.name, l.loan_date
--FROM Loans l
--JOIN Books b ON l.book_id = b.id
--JOIN Members m ON l.member_id = m.id 
--GROUP BY l.id

SELECT b.title, l.*
FROM Books b 
JOIN Loans l ON b.id = l.book_id