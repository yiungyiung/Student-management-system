''' python school project for a student management system'''
import json
import os
import shutil
import sys
from datetime import datetime
montths=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC']
#creates all the required files and chooses the disk/drive where you want to store data    
def createmain():
    classes={}
    Tests={}
    testsdone={}
    testsdone['dates']=[]
    Tests['dates']=[]
    classes['class']=[]
    path=os.path.join(pd,'classes.json')
    with open(path, 'w') as outfile:
        json.dump(classes, outfile)
        with open(pd+'Tests.json','w') as of:
            json.dump(Tests, of)
            with open(pd+'DoneTests.json','w') as ouf:
                json.dump(testsdone, ouf)
#keeps the record of all tests that are done
def donetests(cllass,subdate):
    with open(pd+'DoneTests.json','r+') as f:
                data=json.load(f)
                s=cllass+'-'+subdate
                data['dates'].append(s)
                with open(pd+'DoneTests.json','w') as ouf:
                    json.dump(data, ouf)
#add new testdate for a class                    
def addtestdates(cllass,subdate):
    with open(pd+'Tests.json','r+') as of:
        data=json.load(of)
        s=cllass+'-'+subdate
        data['dates'].append(s)
        with open(pd+'Tests.json','w') as outfile:
            json.dump(data, outfile)
#add new testdate for one student
def addtestonedates(cllass,subdate):
    with open(pd+'Tests.json','r+') as of:
        data=json.load(of)
        s=cllass+'-'+subdate
        data['dates'].append(s)
        with open(pd+'Tests.json','w') as outfile:
            json.dump(data, outfile)
        
def removetestdates(cllass,subdate):
    with open(pd+'Tests.json','r+') as of:
        data=json.load(of)
        s=cllass+'-'+subdate
        j=-1
        for i in data['dates']:
            j+=1
            if i==s:
                del data['dates'][j]
                with open(pd+'Tests.json','w') as outfile:
                    json.dump(data, outfile)
                    donetests(cllass,subdate)
# displays completed tests      
def display_donetests():
    with open(pd+'DoneTests.json','r+') as f:
                data=json.load(f)
                for i in data['dates']:
                    print('class',i)
#displays upcomming tests    
def displayuptests():
    with open(pd+'Tests.json','r+') as of:
        data=json.load(of)
        for i in data['dates']:
            print('class',i)
    
def removetestonedates(cllass,subdate):
    with open(pd+'Tests.json','r+') as of:
        data=json.load(of)
        s=cllass+'-'+subdate
        j=-1
        for i in data['dates']:
            j+=1
            if i==s:
                del data['dates'][j]
        with open(pd+'Tests.json','w') as outfile:
            json.dump(data, outfile)
            donetests(cllass,subdate)
    
    
#displays existing classes    
def display_class():
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        if data['class']==[]:
            print('no class exists')
        else:
            for i in data['class']:
                print('class',i)
#adding new class   
def add_class():
    
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        ss=input('Enter the standard------->').upper().strip()
        while True:
            if ss in data['class']:
                print('Already exists')
                break
            else:
                data['class'].append(ss)
                with open(pd+'classes.json', 'w') as outfile:
                    json.dump(data, outfile)
                d='class'+ss
                p=os.path.join(pd, d)
                os.mkdir(p)
                students={}
                students['names']=[]
                p=os.path.join(p,'studentnames.json')
                with open(p, 'w') as outfile:
                    json.dump(students, outfile)
                    print('process was succesful') 
                break
# adding student to a class      
def add_student():
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        ss=input('Enter the standard------->').upper().strip()
        while True:
            if data['class'] ==[]:
                print('no classes exists')
                break
            elif ss not in data['class']:
                print('class does not exist')
                break
            else:
                s=pd+'class'+ss+'/'
                print('name is the way by which all the studentdata will be identified please enter correctly')
                name=input('name------>').upper().strip()
                a=s+'studentnames.json'
                with open(a,'r+') as jf:
                    d = json.load(jf)
                    while True:
                        
                        if name in d['names']:
                            print('already exists enter again')
                            break
                        else:
                        
                            d['names'].append(name)
                            with open(a,'w') as outfile:
                                json.dump(d, outfile)
                            details={}
                            details['studentdata']=[]
                            dob=input('date of birth in dd/mm/yyyy form---->')
                            connum=input('enter contact number---->')
                            subjects=input('enter subjects seprated by commas---->').upper().strip()
                            fessforsubject=input(f'enter fees for {subjects} seprated by commas---->')
                            l=dict(zip(subjects.split(','),fessforsubject.split(',')))
                            months=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC']
                            a='notpaid '*12
                            m=dict(zip(months,a.split()))
                            details['studentdata'].append({
                                'Name':name,
                                'subjects':l,
                                'months and fees':m,
                                'date of birth':dob,
                                'contact number': connum,
                                'TESTS':{}})

                            name+='.json'
                            p=os.path.join(s, name)
                            with open(p, 'w') as outfile:
                                json.dump(details, outfile)
                                print('process was succesful') 
                            break
                    break
#add tests for a class on specific subject
def addtests():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
        s=input('Enter class---->').upper().strip()
        while True:
            if da['class'] ==[]:
                print('no classes exists')
                break
            elif s not in da['class']:
                print('class does not exist')
                break
            else:
                with open(pd+'/class'+s+'/'+'studentnames.json','r+') as json_file:
                    data = json.load(json_file)
                    x=input('Enter the test subject---->').upper().strip()
                    xa=input('Test date(dd/mm/yy)---->').upper().strip()
                    for i in data['names']:
                        with open(pd+'/class'+s+'/'+i+'.json','r+')as f:
                            d=json.load(f)
                            if x in d['studentdata'][0]['subjects']:
                                if (x+'-'+xa) not in d['studentdata'][0]['TESTS']:
                                    d['studentdata'][0]['TESTS'][x+'-'+xa]='NOT given'
                                    with open(pd+'/class'+s+'/'+i+'.json','w')as of:
                                        json.dump(d,of)
                    
                                else:
                                    print(i,'Already has this test ')
                    addtestdates(s,(x+'-'+xa))
                print('process was succesful')
                break
#add test marks for students
def addtestmarks():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
        s=input('Enter class---->').upper().strip()
        while True:
            if da['class'] ==[]:
                print('no classes exists')
                break
            elif s not in da['class']:
                print('class does not exist')
                break
            else:
                with open(pd+'/class'+s+'/'+'studentnames.json','r+') as json_file:
                    data = json.load(json_file)
                    x=input('Enter the test subject---->').upper().strip()
                    xa=input('Test date(dd/mm/yy)---->').upper().strip()
                    for i in data['names']:
                        with open(pd+'/class'+s+'/'+i+'.json','r+')as f:
                            d=json.load(f)
                            if x in d['studentdata'][0]['subjects']:
                                
                                
                                if (x+'-'+xa) in d['studentdata'][0]['TESTS']:
                                    
                                    
                                    if d['studentdata'][0]['TESTS'][(x+'-'+xa)]=='NOT given':
                                        
                                        aa=input('Enter marks for'+' '+i+' '+x+' test on'+' '+xa+'---->')
                                        d['studentdata'][0]['TESTS'][x+'-'+xa]=aa
                                        with open(pd+'/class'+s+'/'+i+'.json','w')as of:
                                            json.dump(d,of)
                                            
                                    else:
                                        print('Test marks already given for',i)
                                else:
                                    print('Test not assigned for',i)
                 
                removetestdates(s,(x+'-'+xa))
                print('process was succesful')
                break
#you shld get it by the function name duh!!! 
def addtestmarksforonestudnet():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    ss=s
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('Name does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            x=input('Enter the test subject---->').upper().strip()
                            xa=input('Test date(dd/mm/yy)---->').upper().strip()
                            if x in data['studentdata'][0]['subjects']:
                                
                                if (x+'-'+xa) in data['studentdata'][0]['TESTS'] :
                                
                                    if data['studentdata'][0]['TESTS'][(x+'-'+xa)]=='SoloNOT given':
                                        saa=input('Enter marks for'+' '+name+' '+x+' test on'+' '+xa+'---->')
                                        data['studentdata'][0]['TESTS'][x+'-'+xa]=saa
                                        print('marks added')
                                        with open(pd+'class'+s,'w') as of:
                                            json.dump(data,of)
                                        removetestonedates((ss+'-'+name),(x+'-'+xa))
                                        break
                                    else:
                                        print('Test marks already given')
                                        break
                                else:
                                    print('test is not assigned')
                                
                            else:
                                print('subject is not assigned')
                            
                        break
                
            break
#i shld learn how to write function names properly
def edittestmarksforonestudnet():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    ss=s
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('Name does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            x=input('Enter the test subject---->').upper().strip()
                            xa=input('Test date(dd/mm/yy)---->').upper().strip()
                            if (x+'-'+xa) in data['studentdata'][0]['TESTS'] :
                                if data['studentdata'][0]['TESTS'][(x+'-'+xa)]!='NOT given':
                                    aa=input('Enter marks for'+' '+name+' '+x+' test on'+' '+xa+'---->')
                                    data['studentdata'][0]['TESTS'][x+'-'+xa]=aa
                                    print('marks added')
                                    with open(pd+'class'+s,'w') as of:
                                        json.dump(data,of)
                                    break
                                else:
                                    print('Test marks not given')
                                    break
                                
                            else:
                                print('test is not assigned')
                            
                        break
                
            break
def addtestforonestudnet():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    ss=s
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('Name does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            x=input('Enter the test subject---->').upper().strip()
                            xa=input('Test date(dd/mm/yy)---->').upper().strip()
                        
                            if x in data['studentdata'][0]['subjects']:
                                
                                if (x+'-'+xa) not in data['studentdata'][0]['TESTS']:
                                    data['studentdata'][0]['TESTS'][x+'-'+xa]='SoloNOT given'
                                    with open(pd+'class'+s,'w') as of:
                                        json.dump(data,of)
                                    addtestonedates((ss+'-'+name),(x+'-'+xa))
                            
                                else:
                                    print('test is already assigned')
                            else:
                                print('subject not assigned')
                        print('process was successful')
                        break
                
            break
                                         
def display_tests_student():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class']==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('Class does not exist')
            break
        else:
            name=input('name of the student---->').upper().strip()
            a='class'+s+'/'+'studentnames.json'
            with open(pd+a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('does not exists enter again')
                        break
                    else:
                        
                        
                        z=pd+'class'+s+'/'+name+'.json'
                        
                        with open(z,'r+') as jfile:
                            data = json.load(jfile)
                            for i in data['studentdata'][0]['TESTS']:
                                print(i,':',data['studentdata'][0]['TESTS'][i])
                        break
            break        
def display_test_students():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
        s=input('Enter class---->').upper().strip()
        while True:
            if da['class'] ==[]:
                print('no classes exists')
                break
            elif s not in da['class']:
                print('class does not exist')
                break
            else:
                with open(pd+'/class'+s+'/'+'studentnames.json','r+') as json_file:
                    data = json.load(json_file)
                    x=input('Enter the test subject---->').upper().strip()
                    xa=input('Test date(dd/mm/yy)---->').upper().strip()
                    for i in data['names']:
                        with open(pd+'/class'+s+'/'+i+'.json','r+')as f:
                            d=json.load(f)
                            if (x+'-'+xa) in d['studentdata'][0]['TESTS']:
                                print(i,':',x+'-'+xa,':',d['studentdata'][0]['TESTS'][x+'-'+xa])
                                
                break
    
def feespaid():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('name of the student---->').upper().strip()
            a='class'+s+'/'+'studentnames.json'
            with open(pd+a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('does not exists enter again')
                        break
                    else:
                        
                        z=pd+'class'+s+'/'+name+'.json'
                        
                        with open(z,'r+') as jfile:
                            data = json.load(jfile)
                            month=input('Month in 3 letter---->').upper().strip()
                            if month in montths:
                                if len(month) >3:
                                    month=month[:3]
                                now = datetime.now()
                                m=str(now.strftime("%d")).upper().strip()+'/'+str(now.strftime("%b")).upper().strip()
                                data['studentdata'][0]['months and fees'][month]= 'paid on'+m
                                with open(z,'r+') as outfile:
                                    json.dump(data, outfile)
                                    print('process was succesful') 
                                    break
                            else:
                                print('month does not exist try again')
                            
                                
                            
                            
                break

def chkfeespaid():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist---->')
            break
        else:
            name=input('name of the student---->').upper().strip()
            a='class'+s+'/'+'studentnames.json'
            with open(pd+a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('does not exists enter again---->')
                        break
                    else:
                        
                        z=pd+'class'+s+'/'+name+'.json'
                        
                        with open(z,'r+') as jfile:
                            data = json.load(jfile)
                            for i in data['studentdata'][0]['months and fees']:
                                print(i,':',data['studentdata'][0]['months and fees'][i])
                            break
            break
def display_student():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class']==[]:
            print('No classes exist')
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('name of the student---->').upper().strip()
            a='class'+s+'/'+'studentnames.json'
            with open(pd+a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('does not exists enter again')
                        break
                    else:
                        
                        z=pd+'class'+s+'/'+name+'.json'
                        
                        with open(z,'r+') as jfile:
                            data = json.load(jfile)
                            for i in data['studentdata'][0]:
                                if i!='months and fees':
                                    print(i,':',data['studentdata'][0][i])
                            
                        break
            break        
    
        
def display_students():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            with open(pd+'class'+s+'/studentnames.json','r+') as json_file:
                data = json.load(json_file)
                for i in data['names']:
                    with open(pd+'class'+s+'/'+i+'.json','r') as jj:
                        d=json.load(jj) 
                        print(i,': subjects and fees are :',d['studentdata'][0]['subjects'])
                    
            break        
def fees_tht_month():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            
            with open(pd+'/class'+s+'/'+'studentnames.json','r+') as json_file:
                data = json.load(json_file)
                for i in data['names']:
                    with open(pd+'/class'+s+'/'+i+'.json','r+')as f:
                        d=json.load(f)
                        now = datetime.now()
                        m=now.strftime("%b").upper().strip()
                        print(i,':',m,':',d['studentdata'][0]['months and fees'][m])
                
                         
            break
def fees_tht_usermonth():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            month=input('Month in 3 letter---->').upper().strip()
            if month in montths:
                if len(month) >3:
                    month=month[:3]
                with open(pd+'/class'+s+'/'+'studentnames.json','r+') as json_file:
                    data = json.load(json_file)
                    for i in data['names']:
                        with open(pd+'/class'+s+'/'+i+'.json','r+')as f:
                            d=json.load(f)
                            print(i,':',month,':',d['studentdata'][0]['months and fees'][month])
                    break
            else:
                print('Month does not exist Try again')
def changesub():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            subjects=input('enter subjects seprated by commas---->').upper().strip()
                            fessforsubject=input(f'enter fees for {subjects}seprated by commas---->')
                            l=dict(zip(subjects.split(','),fessforsubject.split(',')))
                            data['studentdata'][0]['subjects']=l
                            with open(pd+'class'+s, 'w') as outfile:
                                json.dump(data, outfile)
                                print('process was succesful') 
                            break
            break
def changedob():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('name does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            dob=input('date of birth in dd/mm/yyyy form---->')
                            data['studentdata'][0]['date of birth']=dob
                            with open(pd+'class'+s, 'w') as outfile:
                                json.dump(data, outfile)
                                print('process was succesful') 
                            break
            break
def changeconnum():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('name does not exist enter again')
                        break
                    else:
                        s=s+'/'+name+'.json'
                        with open(pd+'class'+s,'r+') as json_file:
                            data = json.load(json_file)
                            connum=input('enter contact number---->')
                            data['studentdata'][0]['contact number']=connum
                            with open(pd+'class'+s, 'w') as outfile:
                                json.dump(data, outfile)
                                print('process was succesful') 
                            break
            break
def changename():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('name does not exist enter again')
                        break
                    else:
                        xc=pd+'class'+s+'/'+name+'.json'
                        sch=input('Enter the name you want to rename too--->').upper().strip()
                        while True:
                            
                            if sch in d['names']:
                                print('name already exist enter again')
                                sch=input('Enter name again---->').upper().strip()
                            else:
                                j=-1
                                for i in d['names']:
                                    j+=1
                                    if i==name:
                                        d['names'][j]=sch
                                        os.rename(xc,pd+'class'+s+'/'+sch+'.json')
                                        with open(a,'w') as outfile:
                                            json.dump(d,outfile)
                                            print('Process was successful')
                                        break
                                break
                        break
                    
            break                        
    
def delstudent():
    with open(pd+'classes.json','r+') as je:
        da = json.load(je)
    s=input('Enter class---->').upper().strip()
    while True:
        if da['class'] ==[]:
            print('no classes exists')
            break
        elif s not in da['class']:
            print('class does not exist')
            break
        else:
            name=input('Enter name---->').upper().strip()
            a=pd+'class'+s+'/studentnames.json'
            with open(a,'r+') as jf:
                d = json.load(jf)
                while True:
                    if d['names']==[]:
                        print('No students in this class')
                        break
                    elif name not in d['names']:
                        print('name does not exist enter again')
                        break
                    else:
                        yes=input('Do u want to delete this student \"Y"\ for yes and \"N"\ for no ').upper().strip()
                        if yes=='N':
                            print('Going to Delete menu')
                            break
                        elif yes=='Y':
                            s=pd+'class'+s+'/'+name+'.json'
                            os.remove(s)
                            with open(a,'r+') as json_file:
                            
                                data = json.load(json_file)
                                j=-1
                                for i in data['names']:
                                    j+=1
                                    if i ==name:
                
                                        del data['names'][j]
                                        with open(a, 'w') as outfile:
                                            json.dump(data, outfile)
                                            print('process was succesful') 
                                        
                        
                        else:
                            print('Invalid input going to delmenu')
                            break
                        break
            break
            
def delclass():
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        ss=input('Enter the standard---->').upper().strip()
        while True:
            if data['class'] ==[]:
                print('no classes exists')
                break
            if ss not in data['class']:
                print('doesnt exist')
                break
            else:
                yes=input('Do u want to delete this student \"Y"\ for yes and \"N"\ for no ').upper().strip()
                if yes=='N':
                    print('Going to Delete menu')
                    break
                elif yes=='Y':
                    a=ss
                    s=pd+'class'+ss
                    with open(pd+'classes.json','r+') as json_file:
                        data = json.load(json_file)
                        j=-1
                        for i in data['class']:
                            j=j+1
                            if i==a:
                                shutil.rmtree(s)
                                del data['class'][j]
                                with open(pd+'classes.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                    print('process was succesful') 
                                    break
                else:
                    print('invalid input going to delete menu')
                    break
                break
def deleverything():
    print('This will Delete everything')
    u=input('Enter Y to continue and N to stop operation----->').upper().strip()
    while True:
        if u=='Y':
             os.remove('dontdeletestudentsystem.txt')
             shutil.rmtree(pd[0:(len(pd)-1)])
             print("Software deleted Thankyou for using")
             sys.exit()
             break
        elif u=='N':
            break
        else:
            u=input('invalid input enter again').upper().strip()
            
            
def changeclassname():
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        ss=input('Enter the standard---->').upper().strip()
        while True:
            if data['class'] ==[]:
                print('no classes exists')
                break
            elif ss not in data['class']:
                print('doesnt exist')
                break
            else:
                a=input('enter the name of promted class---->')
                while True:
                    if a in data['class']:
                        print('it exists')
                        a=input('Enter the name of promted class again---->').upper().strip()
                    else:
                        j=-1
                        for i in data['class']:
                            j=j+1
                            if ss==i:
                                shutil.move(pd+'class'+ss,pd+'class'+a)
                                data['class'][j]=a
                                with open(pd+'classes.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                    print('process was succesful')
                                    break
                        break
                break
    
   
def promote():
    with open(pd+'classes.json','r+') as json_file:
        data = json.load(json_file)
        ss=input('Enter the standard---->').upper().strip()
        while True:
            if data['class'] ==[]:
                print('no classes exists')
                break
            elif ss not in data['class']:
                print('doesnt exist')
                break
            else:
                a=input('enter the name of promted class---->')
                while True:
                    if a in data['class']:
                        print('class already exists')
                        a=input('Enter the name of promted class again---->').upper().strip()
                    else:
                        
                        with open(pd+'/class'+ss+'/'+'studentnames.json','r+') as jf:
                            d=json.load(jf)
                            for i in d['names']:
                                with open(pd+'class'+ss+'/'+i+'.json','r+') as df:
                                    da=json.load(df)
                                    months=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC']
                                    u='notpaid '*12
                                    m=dict(zip(months,u.split()))
                                    da['studentdata'][0]['months and fees']=m
                                    with open(pd+'class'+ss+'/'+i+'.json','w') as of:
                                        json.dump(da, of)    
                            j=-1
                            for i in data['class']:
                                j=j+1
                                if ss==i:
                                    
                                    data['class'][j]=a
                                    with open(pd+'classes.json', 'w') as outfile:
                                        json.dump(data, outfile)
                                        print('process was succesful')
                                        jf.close()
                                        os.rename(pd+'class'+ss,pd+'class'+a)
                                        break
                        break
                break        
def Testmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========              TEST MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""    
Enter 1 : Add Tests For Students 
Enter 2 : Add Test Marks For Students
Enter 3 : Add Test For A Student
Enter 4 : Add Test Marks For A Student
Enter 5 : Display Marks Of Students For A Subject
Enter 6 : Display Marks Of All Tests Of A Student
Enter 7 : Display Upcoming Tests
Enter 8 : Edit Test marks for a student
Enter 9 : Display all completed tests
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            addtests()

        elif uInp=='2':
            addtestmarks()

        elif uInp=='4':
            addtestmarksforonestudnet()
        elif uInp=='3':
            addtestforonestudnet()
        elif uInp=='6':
            display_tests_student()
        elif uInp=='5':
            display_test_students()
        elif uInp=='7':
            displayuptests()
        elif uInp=='8':
            edittestmarksforonestudnet()
        elif uInp=='9':
            display_donetests()

        elif uInp=='0':
            print('Exiting the Test Menu')
            break

        else:
            print('invalid input try again')                    
def addmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========              ADD MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""    
Enter 1 : Add Class 
Enter 2 : Add Student
Enter 3 : Promote a Class
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            add_class()

        elif uInp=='2':
            add_student()

        elif uInp=='3':
            promote()

        elif uInp=='0':
            print('Exiting the Add Menu')
            break

        else:
            print('invalid input try again')
def editmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========              EDIT MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""    
Enter 1 : Change Subject 
Enter 2 : Change Date Of Birth 
Enter 3 : Change Contact Number
Enter 4 : Change Name
Enter 5 : Change ClassName
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            changesub()
        elif uInp=='2':
            changedob()
        elif uInp=='3':
            changeconnum()
        elif uInp=='4':
            changename()
        elif uInp=='5':
            changeclassname()

        elif uInp=='0':
            print('Exiting Edit Menu')
            break

        else:
            print('invalid input try again')        
def delmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========             DELETE MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""    
Enter 1 : Delete Student 
Enter 2 : Delete Class
Enter 3 : Delete The Software
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            delstudent()

        elif uInp=='2':
            delclass()

        elif uInp=='3':
            deleverything()
            
        elif uInp=='0':
            print('Exiting Edit Menu')
            break

        else:
            print('invalid input try again')        
def dispmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========              DISPLAY MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""
Enter 1 : Display all classes
Enter 2 : Display a Students Data 
Enter 3 : Display all Students of a class 
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            display_class()

        elif uInp=='2':
            display_student()
            
        elif uInp=='3':
            display_students()
        elif uInp=='4':
            display_tests_student()
        
        elif uInp=='0':
            print('Exiting Display Menu')
            break

        else:
            print('invalid input try again')
def feesmenu():
    
    print(""" 

  ------------------------------------------------------
 |                                                      | 
 |========              FEES MENU	        ========|
 |                                                      |
  ------------------------------------------------------ """)
    while True:
        print("""
Enter 1 : Accept The Fees Of A Student
Enter 2 : Check Fees Of All The Months Of A Student  
Enter 3 : Check Fees of One Month Of All Students Of A Class
Enter 5 : Check Fees of One Month Of All Students Of A Class For A Particular Month 
Enter 0 : Go to Main Menu
		
		""")
        uInp = input("Please Select An Above Option: ").upper().strip()
        if uInp=='1':
            feespaid()

        elif uInp=='2':
            chkfeespaid()
            
        elif uInp=='3':
            fees_tht_month()
        elif uInp=='4':
            fees_tht_usermonth()
        
        elif uInp=='0':
            print('Exiting Fees Menu')
            break

        else:
            print('invalid input try again')


try:
    f=open('dontdeletestudentsystem.txt')
    pd=f.read()
    f.close()
except:
    print('Welcome to the Student Management System\nWe have detected that you are using this software for the first time')
    k=input('Enter the Alphabet of the volume you want use for the storage(eg \"C"\or \"D"\)---->').upper().strip()
    j=input('enter the name of the folder you want to create---->').upper().strip()
    a=k+':/'+j
    while True:
        try:
            os.mkdir(a)
            break
        except:
            print('File exists enter again')
            k=input('Enter the Alphabet of the volume you want use for the storage(eg \"C"\or \"D"\)---->').upper().strip()
            j=input('enter the name of the folder you want to create--->').upper().strip()
            a=k+':/'+j
    pd=a+'/'
    createmain()
    with open('dontdeletestudentsystem.txt','w') as f:
        f.write(pd)
    print('You are ready to use the software')
    
print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------
""")
while True:
    
    print("""
Enter 1 : Go to Add Menu 
Enter 2 : Go to Edit Menu 
Enter 3 : Go to Delete Menu 
Enter 4 : Go to Display Menu
Enter 5 : Go to Fees Menu
Enter 6 : Go To Test Menu
Enter 0 : Exit
		
		""")
    uInput = input("Please Select An Above Option: ").upper().strip()
    if uInput=='1':
        addmenu()

    elif uInput=='2':
        editmenu()

    elif uInput=='3':
        delmenu()

    elif uInput=='4':
        dispmenu()

    elif uInput=='5':
        feesmenu()
    elif uInput=='6':
        Testmenu()

    elif uInput=='0':
        print('Exiting the Software')
        break

    else:
        print('invalid input try again')

        
                 
            
