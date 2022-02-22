# s = [['ONE','1'],['TWO',"2"] ,['THR','3'] ,['FOU','4'],['FIV','5'] ,['SIX','6'] ,['SEV','7'],['EIG','8'],['NIN','9'],['ZER','0']]
# def from_word_to_num(a):
#     for i in s:
#         a = a.replace(i[0], i[1])
#     return int(a)
# def from_num_to_word(a):
#     a = str(a)
#     for i in s:
#         a = a.replace(i[1], i[0])
#     return a    
# print(from_num_to_word(sum(list(map(from_word_to_num,input().split('+'))))))