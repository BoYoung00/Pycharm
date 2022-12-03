from score import *

#작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')

def find_student(): # 1-1
    instid = input("> 학번 입력: ")
    val = get_student(instid)
    if val == '':
        print("일치하는 데이터가 없습니다.")
    else:
        sname, deptid = val #리스트 언팩킹
        dname = get_dept(deptid)
        print("학번: %s    성명: %s   소속학과: %s(%s)" %(instid, sname, dname, deptid))

def find_dept(): #1-2
    indeptid = input("> 학과번호 입력 : ")
    dname = get_dept(indeptid)
    if dname == '':
        print("일치하는 데이터가 없습니다.")
    else:
        print("학과명 : %s (%s)" %(dname, indeptid))

def find_prof(): #1-3
    inprof = input("> 교수 아이디 : ")
    dprof = get_prof(inprof)
    if dprof == '':
        print("일치하는 데이터가 없습니다.")
    else:
        fname, fag = dprof
        print("교수 성명 : %s(%s)" %(fname, fag))

def find_subject(): #1-4
    insubject = input("> 과목번호 : ")
    dsubject = get_subject(insubject)
    if dsubject == '':
        print("일치하는 데이터가 없습니다.")
    else:
        dsubject, dcredit, dcode, dpname = dsubject
        print("과목명 : %s     학점 : %s     학과코드 : %s     담당 교수명 : %s" %(dsubject, dcredit, dcode, dpname))

def find_stscore(): #1-5
    a = 0 #일치하지 않는 데이터 찾기용
    instscore = input("> 학번 입력 : ")
    for dclassof, dsubject, dscore in stscore: #학번, 과목코드, 점수
        if instscore in dclassof:
            print("과목코드 : %s      점수 : %s" %(dsubject, dscore))
            a = 1
    if a == 0:
        print("일치하는 데이터가 없습니다.")

def selmenu01_find(): #검색 (1)
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

def write_stugrade(): #2-1
    count = 0 #과목 수
    credit = 0 #학점
    avscore = 0 #평균 점수 (총 점수 더하기)
    rec_save_list = [] #저장할 값 (리스트)

    #타이틀 (학번, 성명, 학과)
    ingrade = input("> 학번 입력 : ")
    val = get_student(ingrade)
    dname, deptid = val  # 리스트 언팩킹 (이름, 학과번호)
    department = get_dept(deptid) #dept(학과이름)에 학과번호가 있는지
    print("_" * 50)
    print("학번 : %s\t 이름 : %s\t 학과 : %s" %(ingrade, dname, department))
    print()
    # 데이터 저장
    rec_title = "학번 : " + ingrade + '\t' "이름 : " + dname + '\t' + "학과 : " + department + '\n'

    #리스트 (과목명, 과목코드, 학점, 점수, 등급)
    print("     과목명\t      과목코드\t  학점\t  점수\t  등급")
    for dclassof, dsubject, dscore in stscore:  # 학번, 과목코드, 점수
        if dclassof in ingrade:
            count += 1 #과목 개수 카운트
            if dsubject in subject:
                dfsubject = get_subject(dsubject) #과목 정보
                ddsubject, dcredit, dcode, dpname = dfsubject #과목명, 학점, 학과코드, 교수아이디
                ddscore = rating(dscore)
                print("%8s\t   %s\t   %s\t   %s\t   %s" % (ddsubject, dsubject, dcredit, dscore, ddscore))

                # 데이터 저장
                data = ddsubject, dsubject, dcredit, dscore, ddscore #데이터 저장을 위한 패킹
                rec_save_list.append(data)

    # 테일 (과목 수, 학점 수, 평균 점수, 평점)
                dcredit = int(dcredit) #학점 int로 변환
                dscore = int(dscore) #점수 int로 변환
                credit = credit + dcredit #총 학점 계산
                avscore = avscore + dscore #총 점수 계산

    # 점수, 평점 계산
    avscore = avscore / count
    ascore = rating(avscore)
    ascore = get_gpoint(ascore)

    # 데이터 타입 변경
    count = str(count)
    avscore = str(round(avscore, 1))
    credit = str(credit)

    print()
    print("과목 수 : %s   학점 수 : %s   평균 점수 : %s   평점 : %s" %(count, credit, avscore, ascore))

    #데이터 저장
    rec_tael = "과목 수 : " + count + '\t' + "학점 수 : " + credit + '\t' + "평균 점수 : " + avscore + '\t' + "평점 : " + ascore + '\n'

    while 1:
        print("_" * 50)
        selno = input("> 내용을 저장하시겠습니까? (1:네   0:아니오) : ")
        if selno == '1' :
            save_situation_score_cs(rec_title, rec_save_list, rec_tael)
            print("저장이 완료되었습니다.")
            break
        elif selno == '0' :
            break
        else:
            print("!잘못된 입력! (1 또는 0을 입력하세요)")
            continue

def write_subgrade(): #2-2
    count = 0 #과목 수
    avscore = 0 #평균 점수
    rec_save_list = []  # 저장할 값 (리스트)

    #타이틀 (과목명, 과목코드, 학점, 개설학과명, 담당교수명)
    insubject = input("> 과목코드 : ") #과목코드
    dsubject = get_subject(insubject)
    dsubject, dcredit, dcode, dpname = dsubject #과목명, 학점, 개설학과코드, 담당교수 아이디

    subname = get_dept(dcode) #개설학과명
    proinfor = get_prof(dpname) #교수 정보(이름 나이)
    proname, proage = proinfor #교수 이름, 나이

    print("_" * 50)
    print("과목명 : %s(%s)   학점 : %s    개설 학과명 : %s    담당 교수명 : %s" % (dsubject, insubject, dcredit, subname, proname))
    #타이틀 데이터 저장
    rec_title = "과목명 : " + dsubject + '(' + insubject + ')' + '\t' + "학점 : " + dcredit + '\t' + "개설 학과명 : " + subname + '\t' + "담당 교수명 : " + proname + '\n'

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

            #리스트 데이터 저장
            data = sname, dclassof, dscore, ddscore #데이터 패킹
            rec_save_list.append(data)

    #테일(학생 수, 평균 점수, 평점)
            intdscore = int(dscore) #점수를 int로 바꿈
            avscore = avscore + intdscore #점수 합계
    avscore = avscore / count #점수 평균 구하기
    ascore = rating(avscore) #평점 구하기
    ascore = get_gpoint(ascore)
    print()
    count = str(count)
    aavscore = str(round(avscore,1))
    print("학생 수 : %s     평균 점수 : %s      평점 : %s" %(count, avscore, ascore))
    rec_teal = "학생 수 : " + count + '\t' + "평균 점수 : " + aavscore + '\t' + "평점 : " + ascore + '\n'

    while 1:
        print("_" * 50)
        selno = input("> 내용을 저장하시겠습니까? (1:네   0:아니오) : ")
        if selno == '1' :
            save_subject_score_cs(rec_title, rec_save_list, rec_teal)
            print("저장이 완료되었습니다.")
            break
        elif selno == '0' :
            break
        else:
            print("!잘못된 입력! (1 또는 0을 입력하세요)")
            continue

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

def stats_subject(): #통계 > 과목별 성적 통계 (3-1)
    count = 0  #수강생 수
    avscore = 0 #평균 점수
    maxscore = [] #최고 점수
    minscore = [] #최저 점수
    rec_save_list = []  # 저장할 값 (리스트)

    #타이틀 (학과명)
    insubject = input("> 학과코드 : ") #학과코드
    sname = get_dept(insubject)

    print("_" * 50)
    print("학과명 : %s(%s)" % (sname, insubject))
    print()
    rec_title = "학과명 : " + sname + '(' + insubject + ')' + '\n'

    #리스트 (과목명, 과목코드, 학점, 수강생 수, 평균 점수, 최고점수, 최저점수)
    print("   과목명       과목코드     학점     수강생 수     평균점수     최고점수     최저점수")
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
            count = str(count)
            aavscore = str(round(aavscore,1))
            maxscore = str(max(maxscore))
            minscore = str(min(minscore))
            print("%s\t    %s\t    %s\t     %2s\t         %s\t     %s\t        %s" %(dsubject, scode, dcredit, count, aavscore, maxscore, minscore))
            data = dsubject, scode, dcredit, count, aavscore, maxscore, minscore
            rec_save_list.append(data)

        count = 0  # 학생수 초기화
        avscore = 0  # 점수 합계 초기화
        maxscore = []  # 최고점수 리스트 초기화
        minscore = []  # 최저점수 리스트 초기화

    while 1:
        print("_" * 50)
        selno = input("> 내용을 저장하시겠습니까? (1:네   0:아니오) : ")
        if selno == '1':
            save_subject_score_stats(rec_title, rec_save_list)
            print("저장이 완료되었습니다.")
            break
        elif selno == '0':
            break
        else:
            print("!잘못된 입력! (1 또는 0을 입력하세요)")
            continue

def stats_professor(): # 통계 > 교수별 담당 과목 통계 (3-2)
    count = 0  # 수강생 수
    sumsubject = 0 # 과목 수
    sumcredit = 0 # 학점 수
    sumstudent = 0 # 수강생 합계
    rec_save_list = [] #저장용 리스트

    # 타이틀 (학과명)
    insubject = input("> 학과코드 : ")  # 학과코드
    sname = get_dept(insubject)

    print("_" * 50)
    print("학과명 : %s(%s)" % (sname, insubject))
    print()
    rec_title = "학과명 : " + sname + '(' + insubject + ')' + '\n'

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
        sumstudent = sumstudent + count
        print("%6s\t    %3s\t   %6s\t   %2s\t      %d" %(dproid, pname, dsubject, dcredit, count))
        dcredit = str(dcredit)
        count = str(count)
        data = dproid, pname, dsubject, dcredit, count
        rec_save_list.append(data)
        count = 0  # 학생수 초기화

    #테일 (과목 수, 학점 수, 수강생 합계)
    sumsubject = str(sumsubject)
    sumcredit = str(sumcredit)
    sumstudent = str(sumstudent)
    print()
    print("과목 수 : %s\t  총 학점 : %s\t  수강생 합계 : %s" %(sumsubject, sumcredit, sumstudent))
    rec_teal = "과목 수 : " + sumsubject + '\t' + "총 학점 : " + sumcredit + '\t' + "수강생 합계 : " + sumstudent + '\n'

    while 1:
        print("_" * 50)
        selno = input("> 내용을 저장하시겠습니까? (1:네   0:아니오) : ")
        if selno == '1':
            save_prof_subject_stats(rec_title, rec_save_list, rec_teal)
            print("저장이 완료되었습니다.")
            break
        elif selno == '0':
            break
        else:
            print("!잘못된 입력! (1 또는 0을 입력하세요)")
            continue

def selmenu03_stats(): #통계 (3)
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

def stscore_format(): #데이터 관리 > 성적 > 수정 (4-1-2)
    print("_" * 50)
    instudent, insubject, inscore = input("> 데이터 입력(학번, 과목코드, 점수) : ").split()
    removedata = [] #지울 데이터 리스트
    indata = [] #추가할 데이터 리스트

    removedata.append(instudent)  # 지울 데이터 리스트로 append하기
    removedata.append(insubject)
    removedata.append(inscore)

    if removedata in stscore: #성적 리스트에 일치하는 데이터가 있는지 확인
        stscore.remove(removedata)  # 성적 리스트에 데이터 지우기

        fstudent, fsubject, fscore = input("> 바뀔 내용 입력(학번, 과목코드, 점수) : ").split() #수정할 내용 받기
        indata.append(fstudent)  # 추가(수정)할 데이터 리스트로 받기
        indata.append(fsubject)
        indata.append(fscore)

        stscore.append(indata)  # 성적 리스트에 추가하기
        print("수정이 완료되었습니다.")
        save_stscore()

    else:
        print("일치하는 데이터가 없습니다.")

def stscore_Additional(): #데이터 관리 > 성적 > 추가 (4-1-3)
    print("_" * 50)
    instudent, insubject, inscore = input("> 추가할 성적 데이터 입력(학번, 과목코드, 점수) : ").split()
    indata = [] #추가할 데이터 리스트

    indata.append(instudent)  # 추가(수정)할 데이터 리스트로 받기
    indata.append(insubject)
    indata.append(inscore)

    stscore.append(indata)  # 성적 리스트에 추가하기
    print("추가가 완료되었습니다.")
    save_stscore()

def stscore_remove(): #데이터 관리 > 성적 > 삭제 (4-1-4)
    instudent, insubject, inscore = input("> 삭제할 성적 데이터 입력(학번, 과목코드, 점수) : ").split()
    inremove = [] #삭제할 데이터 리스트

    inremove.append(instudent)  # 삭제할 데이터 리스트로 받기
    inremove.append(insubject)
    inremove.append(inscore)

    if inremove in stscore:
        stscore.remove(inremove)  # 성적 리스트에서 삭제하기
        print("삭제가 완료되었습니다.")
        save_stscore()
    else:
        print("일치하는 데이터가 없습니다.")

def up_stscore(): #데이터 관리 > 성적
    while True:
        print("_" * 50)
        print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_stscore()
            elif selno == 2:
                stscore_format()
            elif selno == 3:
                stscore_Additional()
            elif selno == 4:
                stscore_remove()
            else:
                print("!잘못된 입력!")

def student_format(): #데이터 관리 > 학생 > 수정 (4-2-2)
    print("_" * 50)
    instudent = input("> 학번 입력 : ")
    removedata_val = []  # 수정 데이터 리스트 값

    if instudent in student: #학생 딕셔너리에 일치하는 데이터가 있는지 확인
        # 수정할 데이터인지 확인용
        val = get_student(instudent)
        sname, deptid = val  # 리스트 언팩킹
        dname = get_dept(deptid)
        print("수정할 학생 정보 > 학번: %s  성명: %s  소속학과: %s(%s)" % (instudent, sname, dname, deptid))
        del student[instudent]  # 확인 후 데이터 삭제

        # 수정할 내용입력(추가)
        fstudent, fname, fdept = input("수정할 학생 정보 입력(학번, 이름, 학과코드) : ").split()
        removedata_val.append(fname) #수정될 값 리스트로 저장
        removedata_val.append(fdept)

        student[fstudent] = removedata_val #학생 딕셔너리에 추가
        print("수정이 완료되었습니다.")
        save_student()

    else:
        print("일치하는 데이터가 없습니다.")

def student_Additional(): #데이터 관리 > 학생 > 추가 (4-2-3)
    add_val = []  # 추가 데이터 리스트 값
    print("_" * 50)
    instudent, inname, indept = input("> 추가할 학생 정보 입력(학번, 이름, 학과코드) : ").split()

    add_val.append(inname)  # 추가될 값 리스트로 저장
    add_val.append(indept)

    student[instudent] = add_val  # 학생 딕셔너리에 추가
    print("추가가 완료되었습니다.")
    save_student()

def student_remove(): #데이터 관리 > 학생 > 삭제 (4-2-4)
    print("_" * 50)
    instudent = input("> 삭제할 학생 정보 입력(학번) : ")

    if instudent in student.keys():
        del student[instudent]
        print("삭제가 완료되었습니다.")
        save_student()
    else:
        print("일치하는 데이터가 없습니다.")

def up_student(): #데이터 관리 > 학생
    while True:
        print("_" * 50)
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

def prof_format(): #데이터 관리 > 교수 > 수정 (4-3-2)
    print("_" * 50)
    inproid = input("> 교수 아이디 입력 : ")
    removedata_val = []  # 수정 데이터 리스트 값

    if inproid in prof: #교수 딕셔너리에 일치하는 데이터가 있는지 확인
        # 수정할 데이터인지 확인용
        val = get_prof(inproid)
        fname, fage = val  # 리스트 언팩킹
        print("수정할 교수 정보 > 아이디 : %s 성명 : %s(%s)" %(inproid, fname, fage))
        del prof[inproid]  # 확인 후 데이터 삭제

        # 수정할 내용입력(추가)
        fstudent, fname, fdept = input("수정할 교수 정보 입력(아이디, 이름, 나이) : ").split()
        removedata_val.append(fname) #수정될 값 리스트로 저장
        removedata_val.append(fdept)

        prof[fstudent] = removedata_val #교수 딕셔너리에 추가
        print("수정이 완료되었습니다.")
        save_prof()
    else:
        print("일치하는 데이터가 없습니다.")

def prof_Additional(): #데이터 관리 > 교수 > 추가 (4-3-3)
    add_val = []  # 추가 데이터 리스트 값
    print("_" * 50)
    inproid, inname, inage = input("> 추가할 교수 데이터 입력(아이디, 이름, 나이) : ").split()

    add_val.append(inname)  # 추가될 값 리스트로 저장
    add_val.append(inage)

    prof[inproid] = add_val  # 학생 딕셔너리에 추가
    print("추가가 완료되었습니다.")
    save_prof()

def prof_remove(): #데이터 관리 > 교수 > 삭제 (4-3-4)
    print("_" * 50)
    inproid = input("> 삭제할 교수 정보 입력(교수 아이디) : ")

    if inproid in prof.keys():
        del prof[inproid]
        print("삭제가 완료되었습니다.")
        save_prof()
    else:
        print("일치하는 데이터가 없습니다.")

def up_prof(): #데이터 관리 > 교수
    while True:
        print("_" * 50)
        print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_prof()
            elif selno == 2:
                prof_format()
            elif selno == 3:
                prof_Additional()
            elif selno == 4:
                prof_remove()
            else:
                print("!잘못된 입력!")

def subject_format(): #데이터 관리 > 과목 > 수정 (4-4-2)
    print("_" * 50)
    insubject = input("> 과목코드 입력 : ")
    removedata_val = [] #데이터 삭제용

    if insubject in subject: #과목 딕셔너리에 일치하는 데이터가 있는지 확인
        # 수정할 데이터인지 확인용
        val = get_subject(insubject)
        dsubject, dcredit, dcode, dproid = val #과목명, 학점, 학과코드, 교수아이디

        print("수정할 과목 정보 > 과목명 : %s   학점 : %s   학과코드 : %s   교수아이디 : %s" %(dsubject, dcredit, dcode, dproid))
        del subject[insubject]  # 확인 후 데이터 삭제

        # 수정할 내용입력(추가)
        fsubcode, fsubject, fcredit, fdept, fproid = input("수정할 과목 정보 입력(과목코드. 과목명, 학점, 학과코드, 교수아이디) : ").split()
        removedata_val.append(fsubject)
        removedata_val.append(fcredit)
        removedata_val.append(fdept)
        removedata_val.append(fproid)

        subject[fsubcode] = removedata_val #과목 딕셔너리에 추가
        print("수정이 완료되었습니다.")
        save_subject()
    else:
        print("일치하는 데이터가 없습니다.")

def subject_Additional(): #데이터 관리 > 과목 > 추가 (4-4-3)
    add_val = []  # 추가 데이터 리스트 값
    print("_" * 50)
    fsubcode, fsubject, fcredit, fdept, fproid = input("추가할 과목 정보 입력(과목코드. 과목명, 학점, 학과코드, 교수아이디) : ").split()

    add_val.append(fsubject)
    add_val.append(fcredit)
    add_val.append(fdept)
    add_val.append(fproid)

    subject[fsubcode] = add_val  # 교수 딕셔너리에 추가
    print("추가가 완료되었습니다.")
    save_subject()

def subject_remove(): #데이터 관리 > 과목 > 삭제 (4-4-4)
    print("_" * 50)
    dsubcode = input("> 삭제할 과목 입력(과목 코드) : ")

    if dsubcode in subject.keys():
        del subject[dsubcode]
        print("삭제가 완료되었습니다.")
        save_subject()
    else:
        print("일치하는 데이터가 없습니다.")


def up_subject(): #데이터 관리 > 과목
    while True:
        print("_" * 50)
        print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_subject()
            elif selno == 2:
                subject_format()
            elif selno == 3:
                subject_Additional()
            elif selno == 4:
                subject_remove()
            else:
                print("!잘못된 입력!")

def dept_format(): #데이터 관리 > 학과 > 수정 (4-5-2)
    print("_" * 50)
    indept = input("> 학과코드 입력 : ")

    if indept in dept: #학과 딕셔너리에 일치하는 데이터가 있는지 확인
        # 수정할 데이터인지 확인용
        ndept = get_dept(indept)
        print("수정할 학과 정보 > 학과이름 : %s   학과코드 : %s" %(ndept, indept))
        del dept[indept]  # 확인 후 데이터 삭제

        # 수정할 내용입력(추가)
        fname, fcode = input("수정할 학과 정보 입력(학과이름, 학과코드) : ").split()

        dept[fcode] = fname #학과 딕셔너리에 추가
        print("수정이 완료되었습니다.")
        save_dept() #파일 저장 함수

    else:
        print("일치하는 데이터가 없습니다.")

def dept_Additional(): #데이터 관리 > 학과 > 추가 (4-5-3)
    print("_" * 50)
    aname, adept = input("추가할 학과 정보 입력(학과명, 학과코드) : ").split()
    dept[adept] = aname
    print("추가가 완료되었습니다.")
    save_dept()

def dept_remove(): #데이터 관리 > 학과 > 삭제 (4-5-4)
    print("_" * 50)
    ddept = input("삭제할 학과 정보 입력(학과 코드) : ")

    if ddept in dept.keys():
        del dept[ddept]
        print("삭제가 완료되었습니다.")
        save_dept()
    else:
        print("일치하는 데이터가 없습니다.")

def up_dept(): #데이터 관리 > 학과
    while True:
        print("_" * 50)
        print("1:검색    2:수정    3:추가    4:삭제   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_dept()
            elif selno == 2:
                dept_format()
            elif selno == 3:
                dept_Additional()
            elif selno == 4:
                dept_remove()
            else:
                print("!잘못된 입력!")

def selmenu04_up(): #데이터 관리
    while True:
        print("_"*50)
        print("1:성적   2:학생   3:교수   4:과목   5:학과   0:복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                up_stscore()
            elif selno == 2:
                up_student()
            elif selno == 3:
                up_prof()
            elif selno == 4:
                up_subject()
            elif selno == 5:
                up_dept()
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