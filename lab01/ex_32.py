teams = ['타이거즈','라이온즈','트윈스','베어스','위즈','렌더스',
         '자이언츠','이글스','다이노스','히어로즈']


# [주의] teams[team]이라고 하지않기
for team in teams:
    print(teams.index(team)+1,team)


i = 1
for team in teams:
    print(i, team)
    i += 1

#enumerate index랑 index에 해당하는 내용이 둘다넘어옴
for i, team in enumerate(teams):
    print(f"{i+1}위 {team}")
