from score import *
#작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')

def find_student():
    instid = input("> 학번 입력: ")
    val = get_student(instid)
    sname, deptid = val #리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" %(instid, sname, dname, deptid))

def find_dept():
    indeptid = input("> 학과번호 입력 : ")
    dname = get_dept(indeptid)
    print("학과명 : %s (%s)" %(dname, indeptid))

def find_prof():
    inprof = input("> 교수 아이디 : ")
    dprof = get_prof(inprof)
    fname, fag = dprof
    print("교수 성명 : %s(%s)" %(fname, fag))

def find_subject():
    insubject = input("> 과목번호 : ")
    dsubject = get_subject(insubject)
    dsubject, dcredit, dcode, dpname = dsubject
    print("과목명 : %s     학점 : %s     학과코드 : %s     담당 교수명 : %s" %(dsubject, dcredit, dcode, dpname))

def find_stscore():
    instscore = input("> 학번 입력 : ")
    for dclassof, dsubject, dscore in stscore: #학번, 과목코드, 점수
        if dclassof in instscore:
            print("과목코드 : %s      점수 : %s" %(dsubject, dscore))

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

def write_stugrade():
    count = 0 #과목 수
    credit = 0 #학점
    avscore = 0 #평균 점수

    #타이틀 (학번, 성명, 학과)
    ingrade = input("> 학번 : ") #학번
    val = get_student(ingrade)
    dname, deptid = val  # 리스트 언팩킹 (이름, 학과번호)
    department = get_dept(deptid) #dept(학과이름)에 학과번호가 있는지
    print("_" * 50)
    print("학번 : %s\t 이름 : %s\t 학과 : %s" %(ingrade, dname, department))
    print()

    #리스트 (과목명, 과목코드, 학점, 점수, 등급)
    print("   과목명\t  과목코드\t  학점\t  점수\t  등급")
    for dclassof, dsubject, dscore in stscore:  # 학번, 과목코드, 점수
        if dclassof in ingrade:
            count += 1; #과목 개수 카운트
            if dsubject in subject:
                dfsubject = get_subject(dsubject) #과목 정보
                ddsubject, dcredit, dcode, dpname = dfsubject #과목명, 학점, 학과코드, 교수아이디
                # print("과목명 : %s   과목코드 : %s    학점 : %s    점수 : %s" %(ddsubject, dsubject, dcredit,dscore))
                ddscore = rating(dscore)
                print("%s\t   %s\t   %s\t   %s\t   %s" % (ddsubject, dsubject, dcredit, dscore, ddscore))

    # 테일 (과목 수, 학점 수, 평균 점수, 평점)
                idcredit = int(dcredit) #학점 int로 변환
                idscore = int(dscore) #점수 int로 변환
                credit = credit + idcredit #총 학점 계산
                avscore = avscore + idscore #총 점수 계산

    avscore = avscore / count
    GPA = rating(avscore)
    print()
    print("과목 수 : %d   학점 수 : %d   평균 점수 : %.1f   평점 : %s" %(count, credit, avscore, GPA))

def write_subgrade():
    count = 0 #과목 수
    avscore = 0 #평균 점수

    #타이틀 (과목명, 과목코드, 학점, 개설학과명, 담당교수명)
    insubject = input("> 과목코드 : ") #과목코드
    dsubject = get_subject(insubject)
    dsubject, dcredit, dcode, dpname = dsubject #과목명, 학점, 개설학과코드, 담당교수 아이디

    subname = get_dept(dcode) #개설학과명
    proinfor = get_prof(dpname) #교수 정보(이름 나이)
    proname, proage = proinfor #교수 이름, 나이

    print("_" * 50)
    print("과목명 : %s(%s)   학점 : %s    개설 학과명 : %s    담당교수명 : %s" % (dsubject, insubject, dcredit, subname, proname))

    #리스트 (학생성명, 학번, 점수, 등급)
    print()
    print("학생성명\t     학번\t  점수\t  등급")

    for dclassof, dsubjnum, dscore in stscore:  # 학번, 과목코드, 점수
        if dsubjnum in insubject: #만약 성적 리스트에 과목코드가 있다면
            count += 1  # 학생수 카운트
            dstudent = get_student(dclassof)
            sname, sdeptcode = dstudent #학생성명, 학과코드
            ddscore = rating(dscore)
            print("%3s\t   %s\t   %s\t   %s\t" %(sname, dclassof, dscore, ddscore))

    #테일(학생 수, 평균 점수, 평점)
            intdscore = int(dscore) #점수를 int로 바꿈
            avscore = avscore + intdscore #점수 합계
    aavscore = avscore / count #점수 평균 구하기
    ascore = rating(aavscore) #평점 구하기
    print()
    print("학생 수 : %d     평균 점수 : %d      평점 : %s" %(count, aavscore, ascore))

def selmenu02_write():
    while True:
        print("_"*50)
        print("1: 학생 성적 현황(학생 성적 통지서)   2: 과목별 성적 현황    0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                write_stugrade()
            elif selno == 2:
                write_subgrade()
            else:
                print("!잘못된 입력!")

def stats_subject():
    count = 0  #수강생 수
    avscore = 0 #평균 점수
    maxscore = 0 #최고 점수
    minscore = 0 #최저 점수

    #타이틀 (학과명)
    insubject = input("> 학과코드 : ") #학과코드
    sname = get_dept(insubject)

    print("_" * 50)
    print("학과명 : %s" % (sname))

    #리스트 (과목명, 과목코드, 학점, 수강생 수, 평균 점수, 최고점수, 최저점수)
    print("   과목명       과목코드       학점      수강생 수      평균 점수      최고점수      최저점수")
    for scode, val in subject.items():
        dsubject, dcredit, dcode, dpname = val #과목명, 학점, 개설학과코드, 담당교수 아이디
        if insubject in dcode: #과목코드 찾기 (키)
            print("%s\t   %s\t   %s\t   " % (dsubject, scode, dcredit))
            #수강생 수, 평균 점수, 최고, 최저 점수 구하기
            for dclassof, dsubjnum, dscore in stscore:  # 학번, 과목코드, 점수
                if scode in dsubjnum:
                    count += 1


def selmenu03_stats():
    while True:
        print("_"*50)
        print("1: 과목별 성적 통계    2: 교수별 담당 과목 통계    0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                stats_subject()
            elif selno == 2:
                stats_subgrade()
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
        selmenu02_write()
    elif selno == STATS:
        selmenu03_stats()
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:          #(x)끝내기
        break
    else:
        break
################################