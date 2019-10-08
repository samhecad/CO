
cnt_total_line = 0
cnt_com_line = 0
cnt_sin_com_line = 0
cnt_block_com_line = 0
cnt_block = 0
cnt_todo = 0
blk_ind = 0

#print(cnt_total_line)


# Counting total number of lines
f = open("source1.txt","r")
cnt_total_line = sum(1 for line in f)


f.close()

# Counting comment lines
f = open("source1.txt","r")

for i in range(0,cnt_total_line):
    str1 = f.readline()
    list1 = str1.split()
    for j in range(0,len(list1)):
        word1 = list(list1[j])
    
        if (word1[0] == '/' or word1[0] == '*' or word1[0] == '#'):
            cnt_com_line = cnt_com_line + 1
            if (i != (cnt_total_line - 1)):
                if (j == 0):
                    blk_ind = blk_ind + 1
                else:
                    cnt_sin_com_line = cnt_sin_com_line + 1
                    blk_ind = 0
                break
            else:
                if (j == 0):
                    blk_ind = blk_ind + 1
                else:
                    cnt_sin_com_line = cnt_sin_com_line + 1
                    blk_ind = 0

                if (blk_ind/2 != 0):
                    cnt_block = cnt_block + 1;
                    cnt_block_com_line = cnt_block_com_line + blk_ind
                else:
                    cnt_sin_com_line = cnt_sin_com_line + blk_ind
                break

     
            
        else:
            if (blk_ind/2 != 0):
                cnt_block = cnt_block + 1;
                cnt_block_com_line = cnt_block_com_line + blk_ind
            else:
                cnt_sin_com_line = cnt_sin_com_line + blk_ind

            blk_ind = 0 # reset block indicator to zero

f.close()

# Counting number of TODOs
f = open("source1.txt","r")

contents = f.read()
cnt_todo = contents.count('TODO')


f.close()

print('Total # of lines: '+ str(cnt_total_line))
print('Total # of comment lines: ' + str(cnt_com_line))
print('Total # of single line comments: ' + str(cnt_sin_com_line))
print('Total # of comment lines within block comments: ' + str(cnt_block_com_line))
print('Total # of block line comments: ' + str(cnt_block))
print('Total # of TODO\'s: ' + str(cnt_todo))
