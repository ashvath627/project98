global sample1_contents, sample2_contents

with open ('sample1.txt') as f1, open('sample2.txt') as f2:
    sample1_contents = f1.read()
    sample2_contents = f2.read()

open('sample1.txt','w').write(sample2_contents)
open('sample2.txt','w').write(sample1_contents)

print('Swapped Files Successfully')
print('file 1: {}, file 2: {}'.format(sample1_contents,sample2_contents))
