
def kmer_probability(n:int):
    return 1/(4**n)

# f = open('results.txt','w+')
# for i in range(1,11):
#     f.write('The probability of any random ' + str(i) + '-mer is ' + str(kmer_probability(i)) + '\n')
# f.close()


def random_kmer_possiblity(target:str, file_name: str):
    '''
    Return the possibility of a specific kmer in a file.
    Using a new search algorithm, rather than str.find()
    '''
    f = open(file_name)
    content = f.readlines()
    valid_str = ''
    for i in content:
        if i[0] == '>':
            continue
        else:
            valid_str += i.strip('\n')
    # my own search algorithm.
    temp = []
    total = 0
    for i in range(len(valid_str)+1):
        poss_kmer = valid_str[i:i+len(target)]
        total += 1
        if poss_kmer == target:
            temp.append(poss_kmer)
    return len(temp)/total

f = open('results.txt','a+')
f.write('\n')
f.write('10-mer\n')
target_kmer = ["ACTAGTTTGC", "CGGACTGTGT", "TGCATCCAAG", "AAGTATGCAA", "GCTAAGATTA"]
for i in range(len(target_kmer)):
    f.write(str(i+1) + '. The possibility of "' + target_kmer[i] + '" in target file is ' + str(random_kmer_possiblity(target_kmer[i], 'Zmay_chr_9-P-94283818.fa')) + '\n')
f.close()



