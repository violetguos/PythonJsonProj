import json
import collections
import csv


def parseStudent(fileName, courseNumberOrName, resultFile = None):
    '''takes a JSON file name, and the courseNumber/course name to query, 
    print out a list of students, also outputs the list to a csv file. Name of CSV file is optional,
    and resultFile name is set to default 'outputStudentList'
    '''
    #parse the file
    with open(fileName) as data_file:    
        data = json.load(data_file)
    
    #from data to a list of student's data
    all_students = data['students'] #type list
    all_courses = data['courses']
    
    
    #a small hash table of courses code to name  
    coursesList={}
    #hash table for course -> list of all students taking it
    coursesNameToCode = {}
    
    #get a short table of course code -> name, used for output formatting       
    for item in all_courses:
        coursesList[item['id']] = item['name']
        coursesNameToCode[item['name']] = item['id']
    
           
    #construct a dictionary/hash table of course code to get a list of student names
    courseStudentList={}
    output = collections.defaultdict(dict)

    #loop through the all_students dictionary
    #create a list of names for each courses number
    #add to dictionary, then query with key(course number) -> student name list in the output printing function
    for item in all_students:
        output[item['name']] = item['courses']
        #tempNameList =[]
        for i in item['courses']: 
            #tempNameList.append(item['name'])
            if i not in courseStudentList:
                courseStudentList[i] = list()        
            courseStudentList[i].append(item['name'])
    
    # do output formmating in another function  
    outputFormatStudents(courseNumberOrName, courseStudentList, coursesNameToCode,coursesList, resultFile)

    return None

def outputFormatStudents(courseNumberOrName, courseStudentList, coursesNameToCode, coursesList, resultFile = None):
    
    '''
    the fucntion takes input, in both course name(string) and course code(int), the parsed hash tables coursesList(courseCoede to course name),
    courseStudentlist(course code to a list of students), and the optional output file name
    
    many type conversion/checking here
    It used to print u'+ studentName
    btw, the prefix 'u' before the output strings just indicates they are unicode, and is not actaully stored in memory.
    Also I fised this with writerow instead of wiretrows
    '''    
    
    
    #you can name this output list or not
    if resultFile != None:
            resultName = resultFile+".csv"
    else:
            resultName = "outputStudentList.csv" 
            
    
    #this block for input courses as string/course names        
    if type(courseNumberOrName) == str:
        courseNum = int(coursesNameToCode[courseNumberOrName])
    else:
        courseNum = courseNumberOrName
            

    #output formatting               
    print("The list of students taking "+ (coursesList[(courseNumberOrName)]))
    print("\n".join(courseStudentList[(courseNumberOrName)]))
    outcsv = open(resultName,'a')
    writer = csv.writer(outcsv)
    writer.writerow(courseStudentList[(courseNumberOrName)])
    #this allows you to append to the csv file, for a list of all courses of 1 prof in parseProf
    #or for any csv file that already exist in the directory
    outcsv.close()
            
    return None    