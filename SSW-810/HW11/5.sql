-- Display each student's name,  CW ID, course, grade, and the instructor's name  for all students and grades.
-- The result should be sorted by the student's name.
-- Hint: You'll need to join the grades and students tables on StudentCWID and CW ID and join the instructors table
-- using the instructor's CW ID.  ' || 'E.g. Bezos, J, CW ID 10115, earned an 'A' in SSW 810 taught by Rowland.

select s.Name, s.CWID, g.Course, g.Grade, i.Name
from student_majors as s
join grades as g on s.CWID = g.StudentCWID
join instructors as i on i.CWID = g.InstructorCWID order by s.Name