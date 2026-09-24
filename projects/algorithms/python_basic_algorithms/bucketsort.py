def bucketsort(data):
    max_score = 0
    for m in data:
        if m[1] > max_score:
            max_score = m[1]
    bucket = [[0,""] for _ in range(max_score+1)]
    for d in data:
        bucket[d[1]][0]+=1
        if len(bucket[d[1]][1]) > 0 :
            bucket[d[1]][1]+=":"+d[0] 
        else:
            bucket[d[1]][1]+=d[0]
    index = 0
    #print(bucket)
    for i in range(len(bucket)):
        if bucket[i][0] != 0:
            sub_index = 0
            for j in range(bucket[i][0]):
                data[index][1] = i
                data[index][0] = bucket[i][1].split(":")[sub_index] if sub_index < len(bucket[i][1].split(":")) else bucket[i][1].split(":")[len(bucket[i][1].split(":"))-1]
                sub_index+=1
                index+=1
            #print(data)
    return data

if __name__ == "__main__":
    data = [['Abby', 58], ['Julia', 44], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], ['Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]
    ans = bucketsort(data)
    print(ans)
