#파일열기
file_to_open = "D:\ReleaseNote\[KOR] T-Solution2 Customer Release Note (v3.510).txt"
f = open(file_to_open, 'r')
lines = f.read().splitlines()

#저장할 파일 열기
file_to_write = file_to_open[:-4] + ".md"
print(file_to_write)
fw = open(file_to_write, 'w')

#새버전 내용만 잘라내기
version_header = "T-Solution 버전:"
new_version_started = False

for line in lines:
    if new_version_started and (-1 != line.find(version_header)): break
    if line.find(version_header) != -1: 
        #새버전 시작줄이니 제목에 #삽입하자.
        new_version_started = True
        line = "# " + line
    if new_version_started:
        # 빈줄이 아니면 줄끝에 공백 2개 삽입하자.
        if len(line): line = line + "  "
        # 세부내용(탭두개)은 공백4개로 바꾸자.
        if line[:2] == "\t\t": line = "    " + line[2:]
        # 항목제목(탭한개)은 삭제하자
        if line[:1] == "\t":   line = line[1:]
        print(line)
        line = line + '\n'
        fw.write(line)
        
f.close()
fw.close()
