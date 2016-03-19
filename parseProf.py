import json
import collections
from parseStudents import parseStudent


def parseProf(fileName, prof, course = None, outputFile =None):
    '''takes a JSON file name, and the professor name to query, print out a list of students and output the list to a csv file
    The third argument is optional. It's used to get only a list of students taking this course out of all courses offered by the profs
    The fourth argument, outputFile is optional, if the user wants to define their own output file name
    '''
    
    #parse the file
    with open(fileName) as data_file:    
        data = json.load(data_file)
    
    #from data to a list of prof's-> course number, course number to name
    all_profs = data['courses']

   
    #a small hash table of courses code to name  
    courseCodeToProf={}
 
    
    #dictionary to a list of course codes, lectured by the prof
    for iterator in all_profs:
        courseCodeToProf[iterator['professor']] = list()
    for iterator in all_profs:    
        courseCodeToProf[iterator['professor']].append(iterator['id'])
    
    #print all student list of all courses the prof teaches, or just one course
    #depend on the optional input
    if(course ==None):
        for i in courseCodeToProf[prof]:
            print("Professor " + prof)
            parseStudent(fileName, i, outputFile) 
    else:
        print("Professor " + prof)
        parseStudent(fileName, course, outputFile)            
  
    return None