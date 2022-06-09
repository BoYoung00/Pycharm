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
    maxscore = [] #최고 점수
    minscore = [] #최저 점수

    #타이틀 (학과명)
    insubject = input("> 학과코드 : ") #학과코드
    sname = get_dept(insubject)

    print("_" * 50)
    print("학과명 : %s" % (sname))

    #리스트 (과목명, 과목코드, 학점, 수강생 수, 평균 점수, 최고점수, 최저점수)
    print("   과목명       과목코드     학점     수강생 수     평균 점수     최고점수     최저점수")
    for scode, val in subject.items():
        dsubject, dcredit, dcode, dpname = val #과목명, 학점, 개설학과코드, 담당교수 아이디
        if insubject in dcode: #과목코드 찾기 (키)
            #수강생 수, 평균 점수, 최고, 최저 점수 구하기
            for dclassof, dsubjnum, dscore in stscore:  # 학번, 과목코드, 점수
                if scode in dsubjnum:
                    dscore = int(dscore) #점수 int로 변환
                    maxscore.append(dscore) #최고점수 리스트로 모으기
                    minscore.append(dscore) #최저점수 리스트로 모으기
                    dscore = int(dscore) #점수 int로 변경
                    avscore = avscore + dscore #점수 합계
                    count += 1 #학생 수
            aavscore = avscore / count
            print("%s\t    %s\t    %s\t     %2d\t         %d\t         %d\t        %d" %(dsubject, scode, dcredit, count, aavscore, max(maxscore), min(minscore)))
        count = 0 #학생수 초기화
        avscore = 0 #점수 합계 초기화
        maxscore = [] #최고점수 리스트 초기화
        minscore = [] #최저점수 리스트 초기화

def stats_professor():
    count = 0  # 수강생 수
    sumsubject = 0 # 과목 수
    sumcredit = 0 # 학점 수
    sumstudent = 0 # 수강생 합계

    # 타이틀 (학과명)
    insubject = input("> 학과코드 : ")  # 학과코드
    sname = get_dept(insubject)

    print("_" * 50)
    print("학과명 : %s" % (sname))
    print()

    # 리스트(교수아이디, 교수명, 과목명, 학점, 수강생 수)
    print("교수아이디    교수명        과목명        학점      수강생 수")
    for scode, val in subject.items(): #과목 딕셔너리 key, val 값 분리
        dsubject, dcredit, dcode, dproid = val #과목명, 학점, 개설학과코드, 담당교수 아이디
        dprof = get_prof(dproid)
        pname, page = dprof #교수명, 나이
        sumsubject += 1 #과목 수 카운트
        dcredit = int(dcredit) #학점 int로 변환
        sumcredit = sumcredit + dcredit #총 학점 카운트
        for dclassof, dsubjnum, dscore in stscore:  # 학번, 과목코드, 점수
            if scode in dsubjnum:
                count += 1  # 학생 수
        print("%6s\t    %3s\t   %6s\t   %2s\t       %d" %(dproid, pname, dsubject, dcredit, count))
        sumstudent = sumstudent + count
        count = 0  # 학생수 초기화

    #테일 (과목 수, 학점 수, 수강생 합계)
    print()
    print("과목 수 : %d\t  학점 수 : %d\t  수강생 합계 : %d\t" %(sumsubject,sumcredit, sumstudent))

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
                stats_professor()
            else:
                print("!잘못된 입력!")

def score_format(): #데이터 관리 > 성적 > 수정 (4-1-2)
    instudent, insubject, inscore = input("> 수정할 데이터 입력(학번, 과목코드, 점수) : ").split()
    removedata = [] #지울 데이터 리스트
    indata = [] #추가할 데이터 리스트

    removedata.append(instudent)  # 지울 데이터 리스트로 append하기
    removedata.append(insubject)
    removedata.append(inscore)

    if removedata in stscore: #성적 리스트에 일치하는 데이터가 있는지 확인
        print("수정할 데이터 > 학번 : %s   과목코드 : %s    점수 : %s"
              %(instudent, insubject, inscore)) #수정할 데이터가 맞는지 확인하는 코드
        stscore.remove(removedata)  # 성적 리스트에 데이터 지우기
        # print(stscore) #지운 결과 값

        fstudent, fsubject, fscore = input("> 수정할 내용(학번, 과목코드, 점수) : ").split() #수정할 내용 받기
        indata.append(fstudent)  # 추가(수정)할 데이터 리스트로 받기
        indata.append(fsubject)
        indata.append(fscore)

        if len(indata[0]) == 6 and len(indata[1]) == 5 and len(indata[2]) == 2:
            stscore.append(indata)  # 성적 리스트에 추가하기
            # print(stscore) #수정된 결과 값
            print("수정이 완료되었습니다.")
            removedata = []  # 지울 데이터 초기화
            indata = []  # 추가할 데이터 초기화 (중복 방지)
        else:
            print("잘못된 내용입니다.(글자 수) ")
            removedata = []  # 지울 데이터 초기화
            indata = []  # 추가할 데이터 초기화 (중복 방지)
    else:
        removedata = [] #지울 데이터 초기화
        print("일치하는 데이터가 없습니다.")

def score_Additional(): #데이터 관리 > 성적 > 추가 (4-1-3)
    instudent, insubject, inscore = input("> 추가할 데이터 입력(학번, 과목코드, 점수) : ").split()
    indata = [] #추가할 데이터 리스트

    indata.append(instudent)  # 추가(수정)할 데이터 리스트로 받기
    indata.append(insubject)
    indata.append(inscore)

    stscore.append(indata)  # 성적 리스트에 추가하기
    # print(stscore) #추가된 결과 값
    print("추가가 완료되었습니다.")

def score_remove(): #데이터 관리 > 성적 > 삭제 (4-1-4)
    instudent, insubject, inscore = input("> 삭제할 데이터 입력(학번, 과목코드, 점수) : ").split()
    inremove = [] #삭제할 데이터 리스트

    inremove.append(instudent)  # 삭제할 데이터 리스트로 받기
    inremove.append(insubject)
    inremove.append(inscore)

    if inremove in stscore:
        stscore.remove(inremove)  # 성적 리스트에서 삭제하기
        # print(stscore) #삭제된 결과 값
        print("삭제가 완료되었습니다.")
        inremove = [] #삭제 데이터 초기화 (중복 방지)

    else:
        print("일치하는 데이터가 없습니다.")
        inremove = []  # 삭제 데이터 초기화 (중복 방지)

def up_score(): #데이터 관리 > 성적
    print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
    selno = input("<작업 선택> ")
    if len(selno) == 0 or selno == '0':
        return
    if len(selno) >= 0 and type(int(selno)) is int:
        selno = int(selno)
        if selno == 1:
            find_stscore()
        elif selno == 2:
            score_format()
        elif selno == 3:
            score_Additional()
        elif selno == 4:
            score_remove()
        else:
            print("!잘못된 입력!")

def student_format(): #데이터 관리 > 학생 > 수정 (4-2-2)
    instudent = input("> 학번 입력 : ")
    removedata_val = []  # 수정 데이터 리스트 값

    if instudent in student: #학생 딕셔너리에 일치하는 데이터가 있는지 확인
        # 수정할 데이터인지 확인용
        val = get_student(instudent)
        sname, deptid = val  # 리스트 언팩킹
        dname = get_dept(deptid)
        print("수정할 내용 > 학번: %s  성명: %s  소속학과: %s(%s)" % (instudent, sname, dname, deptid))
        del student[instudent]  # 확인 후 데이터 삭제

        # 수정할 내용입력(추가)
        fstudent, fname, fdept = input("수정할 내용입력(학번, 이름, 학과코드) : ").split()
        removedata_val.append(fname) #수정될 값 리스트로 저장
        removedata_val.append(fdept)

        student[fstudent] = removedata_val #학생 딕셔너리에 추가
        print("수정이 완료되었습니다.")

        removedata_val = [] #수정 데이터 리스트 초기화 (중복 방지)

    else:
        print("일치하는 데이터가 없습니다.")

def student_Additional(): #데이터 관리 > 학생 > 추가 (4-2-3)
    add_val = []  # 추가 데이터 리스트 값
    instudent, inname, indept = input("> 추가할 데이터 입력(학번, 이름, 학과코드) : ").split()

    add_val.append(inname)  # 추가될 값 리스트로 저장
    add_val.append(indept)

    student[instudent] = add_val  # 학생 딕셔너리에 추가
    print("추가가 완료되었습니다.")
    add_val = []  # 추가 데이터 리스트 초기화 (중복 방지)

def student_remove(): #데이터 관리 > 학생 > 삭제 (4-2-4)
    instudent, inname, indept = input("> 삭제할 데이터 입력(학번, 이름, 학과코드) : ").split()
    remove_val = []  # 삭제할 데이터 리스트
    remove_data = {} # 딕셔너리

    remove_val.append(inname)  # 삭제할 값 리스트로 저장 (비교를 위해 선언)
    remove_val.append(indept)

    remove_data[instudent] = remove_val
    print(remove_data)

    if remove_data.items() in student.items():
        del student[instudent]
        print("삭제가 완료되었습니다.")
        # remove_val = []  # 데이터 리스트 초기화 (중복 방지)
        # remove_data = {}  # 딕셔너리 초기화 (중복 방지)
    else:
        print("일치하는 데이터가 없습니다.")

def up_student(): #데이터 관리 > 학생
    print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
    selno = input("<작업 선택> ")
    if len(selno) == 0 or selno == '0':
        return
    if len(selno) >= 0 and type(int(selno)) is int:
        selno = int(selno)
        if selno == 1:
            find_student()
        elif selno == 2:
            student_format()
        elif selno == 3:
            student_Additional()
        elif selno == 4:
            student_remove()
        else:
            print("!잘못된 입력!")

def selmenu04_up(): #데이터 관리
    while True:
        print("_"*50)
        print("1:성적   2:학생   3:교수   4:과목   5:수강   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                up_score()
            elif selno == 2:
                up_student()
            elif selno == 3:
                up_task()
            elif selno == 4:
                up_task()
            elif selno == 5:
                up_task()
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
while True:    #작업 선택
    selno = sel_task()  #작업 번호 선택
    if selno == SEARCH:
        selmenu01_find()
    elif selno == LIST:
        selmenu02_write()
    elif selno == STATS:
        selmenu03_stats()
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:     #(x)끝내기
        break
    else:
        break
################################