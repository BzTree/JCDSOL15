# -*- coding: utf-8 -*-
"""Capstone project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eq_vxskWI9BpJ3_4YCkD_0MeEw2waTh9
"""

# Making database for Data Nilai Siswa

#!pip install tabulate
#!pip install regex
#!pip install sys

from tabulate import tabulate
import regex
import sys

# Dummy data
StudentMarks = [{'No':1, 'Studentid':'OL01-1', 'Name':'Mark', 'Surname':'Seagal', 'Science':90, 'Math':80, 'English':70},
  {'No':2, 'Studentid':'OL01-2', 'Name':'Anne', 'Surname':'Mason', 'Science':85, 'Math':77, 'English':99},
  {'No':3, 'Studentid':'OL01-3', 'Name':'John', 'Surname':'Horner', 'Science':88, 'Math':79, 'English':78},
  {'No':4, 'Studentid':'OL01-4', 'Name':'Jason', 'Surname':'Wankel', 'Science':90, 'Math':99, 'English':60},
  {'No':5, 'Studentid':'OL01-5', 'Name':'Mikhail', 'Surname':'Antonov', 'Science':99, 'Math':99, 'English':55}]

# Global variables
TemporaryStorage = []

FilteredStudentMarks = StudentMarks

Counter = len(FilteredStudentMarks)
StudentIDCounter = len(FilteredStudentMarks)
SchoolCode = 'OL01-'

# Small Task Functions:
# Checks if the input is only alphabets, then makes them proper case.
def AlphaChecker(Column):
  while True:
    text = input(f'Please {Column}:')
    GoBack(text)
    if text.isalpha() == False:
      print('Invalid input. Please input letters only. ')
      continue
    else:
      text = text.lower()
      text = text.capitalize()
      return text

# Checks if the input is only digits, then turns them into 'int'.
def DigitChecker(Column):
  while True:
    number = input(f'Please {Column}:')
    GoBack(number)
    if number.isdigit() == True:
      number = int(number)
      return number
    else:
      print('Invalid input. Please input non-negative numbers only. ')
      continue

# DigitChecker() that disallows values over 100.
def MarkChecker(Column):
  while True:
    mark = input(f'Please {Column} marks:')
    GoBack(mark)
    if mark.isdigit() == True:
      mark = int(mark)
      if mark > 100:
        print('Marks cannot be over 100. ')
      else:
        int(mark)
        return mark
    else:
      print('Invalid input. Please input non-negative numbers only. ')
      continue

# Reassigns the 'No' Column for all entries whenever the table is rearranged, ensuring they always go in ascending order from the top.
def ReNo(FilteredStudentMarks):
  for i in range(len(FilteredStudentMarks)):
    FilteredStudentMarks[i]['No'] = i + 1
    Counter = len(FilteredStudentMarks)

# Lets the user go back to main() at any point in the program by pressing 'm'.
def GoBack(Thing):
  if Thing == 'm':
    print('returning to main menu...')
    main()

# Lets the user see all the services available in main() by pressing '7'.
def ShowServices():
    print('1. Add Student')
    print('2. Modify Student')
    print('3. View, Sort or Filter Database')
    print('4. Delete Entry')
    print('5. Restore/Permanently Delete Entries')
    print('6. Change School Code')
    print('7. Show List of Services Again')
    print('8. Save Table')
    print('9. Exit')
    print("Note: You can always return to this menu by pressing 'm'.")

## Must have:
## Way to add new entry
def AddStudent():
  Name = AlphaChecker('enter Name')
  Surname = AlphaChecker('enter Surname')
  Science = MarkChecker('enter Science')
  Math = MarkChecker('enter Math')
  English = MarkChecker('enter English')
  global Counter
  Counter += 1
  ID = Counter
  global StudentIDCounter
  StudentIDCounter += 1
  FilteredStudentMarks.append({'No': ID, 'Studentid':SchoolCode+str(StudentIDCounter), 'Name': Name, 'Surname': Surname, 'Science': Science, 'Math': Math, 'English': English})
  print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
  print('New entry successfully added.')

## Way to modify entry
def ModifyTarget():
  print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
  while True:
    Row = DigitChecker('enter the number (No) of the student entry you want to modify')
    if Row > len(FilteredStudentMarks):
      print('That row is not present in this table. Please try again.')
      continue
    else:
      Row = Row - 1
    while True:
      Column = AlphaChecker('enter the name of the column to modify')
      Column.capitalize()
      if Column in ['No','Studentid']:
        print("Sorry, those columns can't be changed.")
        continue
      if Column in ['Name', 'Surname']:
        FilteredStudentMarks[Row][Column] = AlphaChecker(f'enter {Column}')
      elif Column in ['Science', 'Math', 'English']:
        FilteredStudentMarks[Row][Column] = MarkChecker(f'enter {Column}')
      else:
        print('That column is not present in the table. Please try again.')
        continue
      print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
      print('Entry successfully modified.')
      return

## Way to view whole database and sort and filter results
def ViewSortFilterDatabase():
  print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
  while True:
    print('Would you like to sort or filter?')
    print('Please press 1 for sorting')
    Sort = DigitChecker('press 2 for filtering')
    if Sort == 1:
      SortBy()
    elif Sort == 2:
      FilterBy()
    else:
      print('Invalid input. Please input either 1 or 2.')
      continue
    return


## Way to delete entry
def DeleteEntry():
  print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
  print('Which student entry do you want to delete?')
  while True:
    Delete = DigitChecker('specify the number (No) of the row')
    global Counter
    if Delete <= Counter and Delete > 0:
      Delete = int(Delete) - 1
      TemporaryStorage.append(FilteredStudentMarks[Delete])
      FilteredStudentMarks.pop(Delete)
      print('Entry successfully deleted.')
      ReNo(FilteredStudentMarks)
      ReNo(TemporaryStorage)
      Counter -= 1
      print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
      return
    else:
      print('That row is not present in this table. Please try again.')
      continue

## Extra functionalities
### Sorting functionality
def SortBy():
  print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
  while True:
    Column = AlphaChecker('enter column you would like to sort by')
    Column = Column.capitalize()
    if Column not in FilteredStudentMarks[0].keys():
      print('That column is not present in the table. Please try again.')
      continue
    else:
      print('Would you like to sort ascending or descending?')
      print('Please press 1 for ascending')
      Sort = DigitChecker('press 2 for descending')
      if Sort == 1:
        FilteredStudentMarks.sort(key = lambda x: x[Column])
      elif Sort == 2:
        FilteredStudentMarks.sort(key = lambda x: x[Column], reverse = True)
      else:
        print('Invalid input. Please input either 1 or 2.')
        continue
      ReNo(FilteredStudentMarks)
      print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
      print('Table successfully sorted.')
      return

### Filtering functionality
def FilterBy():
    global FilteredStudentMarks
    TempFSM = []
    while FilteredStudentMarks != StudentMarks:
      print('It seems that the current table is different from the unfiltered one. Would you like to restore the unfiltered one?')
      YesOrNo = AlphaChecker('enter Yes or No')
      if YesOrNo == 'Yes':
        FilteredStudentMarks = StudentMarks
        print('Filter cleared.')
        print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
        ReNo(FilteredStudentMarks)
      elif YesOrNo == 'No':
        print('Filter not cleared.')
        break
      else:
        print('This entry is neither Yes nor No.')
        continue
    while True:
      print('What column would you like to filter by? ')
      Filter = AlphaChecker('enter column')
      Filter.capitalize()
      if Filter in ['Studentid']:
        print("Sorry, we can't filter using this column as of now.")
        continue
      if Filter in ['Name','Surname']:
        FilterList = AlphaChecker('enter the starting letters of the names that will be kept')
        for i in range(len(FilteredStudentMarks)):
          if FilterList in FilteredStudentMarks[i][Filter]:
            TempFSM.append(FilteredStudentMarks[i])
      elif Filter in ['No','Science','Math','English']:
        FilterList = MarkChecker('enter the student number or')
        print('Do you want to show all results above or below this mark? ')
        print('Please press 1 for above')
        Sign = DigitChecker('press 2 for below')
        if Sign == 1:
          for i in range(len(FilteredStudentMarks)):
            if FilteredStudentMarks[i][Filter] >= FilterList:
              TempFSM.append(FilteredStudentMarks[i])
        elif Sign == 2:
          for i in range(len(FilteredStudentMarks)):
            if FilteredStudentMarks[i][Filter] <= FilterList:
              TempFSM.append(FilteredStudentMarks[i])
        else:
          print('Invalid input. Please input either 1 or 2.')
          continue
      else:
        print('That column is not present in the table. Please try again.')
        continue
      FilteredStudentMarks = TempFSM
      ReNo(TempFSM)
      print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
      return

### Ability to restore deleted entries, or delete them for good
def Restoration():
  print(tabulate(TemporaryStorage, headers = 'keys', tablefmt = 'pretty'))
  while True:
    if TemporaryStorage == []:
      print('There is nothing in the backup. You have either restored or deleted them all.')
      return
    else:
      print('Would you like to restore these entries or permanently delete them?')
      print('Please press 1 for restoring')
      Restore = DigitChecker('press 2 for permanently deleting')
      if Restore == 1:
        Row = DigitChecker('enter the number (No) of the row')
        if Row > len(TemporaryStorage):
          print('That row is not present in this table. Please try again.')
          continue
        else:
          FilteredStudentMarks.append(TemporaryStorage[Row - 1])
          ReNo(FilteredStudentMarks)
          TemporaryStorage.pop(Row - 1)
          print(tabulate(FilteredStudentMarks, headers = 'keys', tablefmt = 'pretty'))
          print('Entry successfully restored.')
          print('Would you like to restore more entries?')
          YesOrNo = AlphaChecker('enter Yes or No')
          if YesOrNo == 'Yes':
            continue
          elif YesOrNo == 'No':
            return
          else:
            print('This entry is neither Yes nor No.')
            continue
      elif Restore == 2:
        print('Are you sure you want to permanently delete these entries?')
        YesOrNo = AlphaChecker('enter Yes or No')
        if YesOrNo == 'Yes':
          TemporaryStorage.clear()
          print('Entries successfully deleted.')
          return
        elif YesOrNo == 'No':
          continue
        else:
          print('This entry is neither Yes nor No.')
          continue
      else:
        print('Invalid input. Please enter either 1 or 2.')
        

### Ability to change school code
def ChangeSchoolCode():
  global SchoolCode
  print(f"Current school code: '{SchoolCode}'")
  SchoolCode = input('enter new school code: ')
  if regex.findall(r'-', SchoolCode) == []:
    SchoolCode = SchoolCode + '-'
  print(f"School code succesfully changed. It is now '{SchoolCode}'.")
  return

###  Main function that ties all the functions together
def main():
  print('Welcome to Student Marks Management System.')
  ShowServices()
  while True:
    print("You can open up the list of services this program provides by pressing '7'.")
    menu = DigitChecker('the number of the service you want to use')
    if menu == 1:
      AddStudent()
      continue
    elif menu == 2:
      ModifyTarget()
      continue
    elif menu == 3:
      ViewSortFilterDatabase()
      continue
    elif menu == 4:
      DeleteEntry()
      continue
    elif menu == 5:
      Restoration()
      continue
    elif menu == 6:
      ChangeSchoolCode()
      continue
    elif menu == 7:
      ShowServices()
      continue
    elif menu == 8:
      StudentMarks = FilteredStudentMarks
      print('Table successfully saved.')
      continue
    elif menu == 9:
      print('Program has been terminated. Thank you for using the Student Marks Management System.')
      sys.exit()
    else:
      print('Invalid input. Please input the correct number. ')
      continue

main()
