select  s.CWID, s.Name, count(g.Course) as No_of_Course from student_majors as s
join grades as g where g.StudentCWID = s.CWID group by  s.CWID