import os

#평점 딕셔너리
gpoint = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

#학과 딕셔너리
dept = {'10': '행정과', '11': '복지학과', '20': '스포츠학과', '21': '간호학과', '30': '컴소과', '31': '전자공학과', '32': '건축과'}

#교수 딕셔너리
prof = {'utlim': ['임국진', '50'], 'lee': ['이성우', '43'], 'hong': ['홍사인', '45'], 'parking': ['박찬우', '38']}

#과목 딕셔너리
subject = {'30101': ['소프트웨어원리', '3', '30', 'utlim'], '30102': ['컴퓨터구조', '3', '30', 'hong'], '30201': ['컴퓨터그래픽', '3', '30', 'lee']}

#학생 딕셔너리
student = {'2230001': ['이우주', '30'], '2230002': ['김사랑', '30'], '2230003': ['강수아', '30'], '2230004': ['박홍이', '30'],
           '2230005': ['하준', '30'], '2230006': ['서민정', '30'], '2230007': ['기수림', '30'], '2230008': ['나민영', '30'],
           '2230009': ['최사랑', '30'], '2230010': ['이보배', '30']}
#성적 리스트
stscore = [['2230001', '30101', '86'], ['2230002', '30101', '90'], ['2230003', '30101', '92'], ['2230004', '30101', '80'],
           ['2230005', '30101', '65'], ['2230006', '30101', '84'], ['2230007', '30101', '75'], ['2230008', '30101', '95'],
           ['2230009', '30101', '90'], ['2230010', '30101', '50'], ['2230001', '30102', '80'], ['2230002', '30102', '89'],
           ['2230003', '30102', '95'], ['2230004', '30102', '77'], ['2230005', '30102', '70'], ['2230006', '30102', '85'],
           ['2230007', '30102', '85'], ['2230008', '30102', '90'], ['2230009', '30102', '88'], ['2230010', '30102', '60'],
           ['2230001', '30201', '96'], ['2230002', '30201', '91'], ['2230003', '30201', '93'], ['2230006', '30201', '85'],
           ['2230007', '30201', '85'], ['2230008', '30201', '90'], ['2230009', '30201', '80'], ['2230010', '30201', '80']]

#학과 딕셔너리 저장
def save_dept():
    fpath = os.getcwd()
    fname = fpath + '\\' + "dept.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for key, val in dept.items():
            rec = key + '\t' + val + '\n'
            f.write(rec)

#교수 딕셔너리 저장
def save_prof():
    fpath = os.getcwd()
    fname = fpath + '\\' + "prof.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for key, val in prof.items():
            pname, page = val
            rec = key + '\t' + pname + '\t' + page + '\n'
            f.write(rec)

#과목 딕셔너리 저장
def save_subject():
    fpath = os.getcwd()
    fname = fpath + '\\' + "subject.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for key, val in subject.items():
            dsubject, dcredit, dcode, dpname = val
            rec = key + '\t' + dsubject + '\t' + dcredit + '\t' + dcode + '\t' + dpname + '\n'
            f.write(rec)

#학생 딕셔너리 저장
def save_student():
    fpath = os.getcwd()
    fname = fpath + '\\' + "student.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for key, val in student.items():
            sname, deptid = val
            rec = key + '\t' + sname + '\t' + deptid + '\n'
            f.write(rec)

#성적 리스트 저장
def save_stscore():
    fpath = os.getcwd()
    fname = fpath + '\\' + "stscore.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for dclassof, dsubject, dscore in stscore:
            rec = dclassof + '\t' + dsubject + '\t' + dscore + '\n'
            f.write(rec)

#평점 딕셔너리 저장
def save_gpoint():
    fpath = os.getcwd()
    fname = fpath + '\\' + "gpoint.txt"
    with open(fname, 'w', encoding='UTF-8') as f:
        for key, val in gpoint.items():
            val = str(val)
            rec = key + '\t' + val + '\n'
            f.write(rec)

#학과 딕셔너리 저장
def read_dept():
    fpath = os.getcwd()
    fname = fpath + '\\' + "dept.txt"
    with open(fname, 'r', encoding='UTF-8') as f:
        for key, val in dept.items():
            rec = key + '\t' + val + '\n'
            f.write(rec)

#학생 성적 현황 저장
def save_situation_score(title, list, teal):
    print(title, list, teal)
    inname = input("> 파일 이름 입력 : ")
    fpath = os.getcwd()
    fname = fpath + '\\' + inname + ".txt"

    result = ""
    for s in list:
        result += s + " "
    print(result)
    # alist = list.split(',')
    # with open(fname, 'a', encoding='UTF-8') as f:
    #     f.write(title)
    #     for x in alist:
    #         f.write(x + '\n')
    #     f.write(teal)

def get_student(stid):
    if stid in student.keys():
        val = student.get(stid)
        return val
    else:
        return ''

def get_dept(deptid):
    if deptid in dept.keys():
        val = dept.get(deptid)
        return val
    else:
        return ''

def get_prof(profid):
    if profid in prof.keys():
        val = prof.get(profid)
        return val
    else:
        return ''

def get_subject(subid):
    if subid in subject.keys():
        val = subject.get(subid)
        return val
    else:
        return ''

def get_gpoint(score):
    if score in gpoint.keys():
        val = gpoint.get(score)
        return val
    else:
        return ''

def rating(ascore): #등급 구하기
    asc = int(ascore)
    if asc >= 95:
        return 'A+'
    elif asc >= 90:
        return 'A'
    elif asc >= 85:
        return 'B+'
    elif asc >= 80:
        return 'B'
    elif asc >= 75:
        return 'C+'
    elif asc >= 70:
        return 'C'
    elif asc >= 65:
        return 'D+'
    elif asc >= 60:
        return 'D'
    else:
        return 'F'

# save_dept()
# save_prof()
# save_subject()
# save_student()
# save_stscore()
# save_gpoint()