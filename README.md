This part of the README applies to the first capstone project only.

The code made for this project is made for teachers who want to keep track of the marks their students get at exams, with the assumption that the school's marks only go up to 100 and the teacher only has to take care of a class of students, though it is possible to use this
for the whole school, but it might not work properly if this is the case.

You need to install the following for this to work:
1. tabulate
2. regex
3. sys

The columns on the table used for this project are:
1. No: This is a simple number that helps the user know what number to input to call its corresponding entry.
2. Studentid: This registers the ID of the student. A dummy Studentid is used in this project.
3. Name: The name of the student.
4. Surname: The surname of the student.
5. Science: The science marks the student got in the exam.
6. Math: The math marks the student got in the exam.
7. English: The English marks the student got in the exam.

The main functions of this code is as follows:
1. Adding entries to the table via the AddStudent() function.
2. Modifying single keys of an entry via the ModifyTarget() function.
3. Deleting an entry via the DeleteEntry() function.
4. Viewing the table via the ViewDatabase() function, also allows sorting via the SortBy() function and filtering via the FilterBy() function.
5. Allows the restoration or permanent deletion of deleted entries via the Restoration() function.
6. Change the school code via the ChangeSchoolCode() function (The school code is the part of the Studentid that is on the left side of the dash ('-') symbol).

A few extra mini-features of this program are:
1. All text-related inputs are turned into proper case using the AlphaChecker() function, which is used on almost all inputs where only letters are expected.
2. Any inputs where only digits are expected use the DigitChecker() function. MarkChecker() has the same functionality plus a limit to disallow integers over 100.
3. There is a ReNo() function that refreshes the 'No' column everytime the table's contents change (The Studentid column is not touched).
4. The GoBack() function is called in the AlphaChecker(), DigitChecker() and MarkChecker() functions to allow the user to go back to main() whenever they want.
5. The ShowServices() function works only in the main() function, where it is used to bring up all the numbers that correspond to the services available in this code.
