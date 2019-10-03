
cnt_total_line = 0
cnt_com_line = 0
cnt_sin_com_line = 0
cnt_block_com_line = 0
cnt_block = 0
cnt_todo = 0
blk_ind = 0

#print(cnt_total_line)


# Count total number of lines
f = open("source1.txt","r")
cnt_total_line = sum(1 for line in f)


f.close()

f = open("source1.txt","r")


for i in range(0,cnt_total_line):
    str1 = f.readline()
    list1 = str1.split()
    word1 = list(list1[0])
    #while (i != (cnt_total_line - 1))
    if (word1[0] == '/' or word1[0] == '*' or word1[0] == '#'):
        cnt_com_line = cnt_com_line + 1
        blk_ind = blk_ind + 1
    else:
        if (blk_ind/2 != 0):
            cnt_block = cnt_block + 1;
            cnt_block_com_line = cnt_block_com_line + blk_ind 
        else:
            cnt_sin_com_line = cnt_sin_com_line + blk_ind

        blk_ind = 0 # reset block indicator to zero
    



f.close()

print(cnt_total_line)
print(cnt_com_line)
print(cnt_sin_com_line)
print(cnt_block_com_line)
print(cnt_block)
