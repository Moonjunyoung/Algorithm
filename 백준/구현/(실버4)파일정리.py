n=int(input())

extension_list=dict()
for i in range(n):
    file=input().split('.')
    if file[1] not in extension_list:
        extension_list[file[1]]=1
    else:
        extension_list[file[1]]+=1



tmp=sorted(extension_list.keys())
for i in tmp:
    print(i,extension_list[i])