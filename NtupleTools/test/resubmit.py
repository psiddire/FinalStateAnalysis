file = open("farmout.txt","r+")
for line in file.readlines():
    word = line.split()
    if word[4]=='0' and word[3]!='0':
        print 'farmoutAnalysisJobs --rescue-dag-file /nfs_scratch/psiddire/MC2017/'+word[0]+'/dags/dag'
    
