% Facts: student(Name, RollNo).
student(alice, 101).
student(bob, 102).
student(charlie, 103).

% teacher(Name, SubjectCode).
teacher(smith, cs101).
teacher(jones, ma102).
teacher(lee, ph103).

% teaches(SubjectCode, SubjectName).
teaches(cs101, 'Computer Science').
teaches(ma102, 'Mathematics').
teaches(ph103, 'Physics').

% enrolled(RollNo, SubjectCode).
enrolled(101, cs101).
enrolled(102, ma102).
enrolled(103, ph103).
enrolled(101, ma102).

% Rules

% Find teacher for a student's subject
student_teacher(Student, Teacher) :-
    student(Student, Roll),
    enrolled(Roll, Sub),
    teacher(Teacher, Sub).

% Find subject name for a student
student_subject(Student, Subject) :-
    student(Student, Roll),
    enrolled(Roll, Code),
    teaches(Code, Subject).
