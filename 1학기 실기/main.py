from score import *
#작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')

def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val #리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" %(instid, sname, dname, deptid))

def find_dept():
    indeptid = input("> 학과번호 입력 : ")
    dname = get_dept(indeptid)
    print("학과명 : %s (%s)" %(dname, indeptid))

def find_prof():
    inprof = input("> 교수님 성함 : ")
    dprof = get_prof(inprof)
    fname, fag = dprof
    print("교수님 성함 : %s (%s)" %(fname, fag))

def find_subject():
    insubject = input("> 과목번호 : ")
    dsubject = get_subject(insubject)
    dsubject, dctime, dfctime, dpname = dsubject
    print("과목명 : %s     수업시간 : %s     수업 총시간 : %s     교수님 성함 : %s" %(dsubject, dctime, dfctime, dpname))

def find_stscore():
    instscore = input("> 학번 : ")
    for dclassof, dsubject, dscore in stscore:
        if dclassof in instscore:
            print("과목번호 : %s      점수 : %s" %(dsubject, dscore))

def selmenu01_find():
    while True:
        print("_"*50)
        print("1: 학생검색    2: 학과검색    3: 교수검색    4: 과목검색    5: 성적검색    0: 복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_student()
            elif selno == 2:
                find_dept()
            elif selno == 3:
                find_prof()
            elif selno == 4:
                find_subject()
            elif selno == 5:
                find_stscore()
            else:
                print("!잘못된 입력!")

def find_stscore():
    instscore = input("> 학번 : ")
    for dclassof, dsubject, dscore in stscore:
        if dclassof in instscore:
            print("과목번호 : %s      점수 : %s" %(dsubject, dscore))

def selmenu02_find():
    while True:
        print("_"*50)
        print("1:학생 성적 현황(학생 성적 통지서)   2:과목별 성적 현황    0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_student()
            elif selno == 2:
                find_dept()
            else:
                print("!잘못된 입력!")

def sel_task(): #작업 선택 메뉴
    print("_"*50)
    print("1:검색   2:현황   3:통계   4:데이터관리   x:종료")
    selno = input("<작업 선택> ")
    if len(selno) == 0:
        return 'x'
    else:
        return selno

########## Main ################
while True:         #작업 선택
    selno = sel_task()      #작업 번호 선택
    if selno == SEARCH:
        selmenu01_find()
    elif selno == LIST:
        selmenu02_find()
    elif selno == STATS:
        print(STATS)
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:          #(x)끝내기
        break
    else:
        break
################################