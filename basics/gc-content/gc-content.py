fastaFile = open('./rosalind_gc.txt').read()
fastaParsed=[]
def parser(file):
  arr = []
  count = 0
  geneId = ''
  gene = ''
  for char in file:
    count = count+1
    if char == '>':
      if count > 1:
        arr.append([geneId, gene])
      count = 0
      geneId = ''
      gene = ''
    if count<14:
      geneId = geneId+char
    if char != '\n' and count>15:
      gene = gene+char

  return arr

def gcCounter(parsedFasta):
  for gen in parsedFasta:
    gen.append(0) 
    for char in gen[1]:
      if char == 'C' or char == "G":
        gen[2] = gen[2] + 1
  return parsedFasta

def getHighest(countCG):
  prevValue = 0
  highest = ''
  for gen in countCG:
    if gen[2] > prevValue:
      prevValue = gen[2]
      highest = gen
     
  a = len(highest[1])
  gcContent =  highest[2] / (a / 100.0)

  return [highest[0], gcContent]

parsedFasta = parser(fastaFile)

countCG = gcCounter(parsedFasta)
print(getHighest(countCG))

fastaFile = open('./rosalind_hamm.txt').read()
genes = []
def read_fasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

with open('./rosalind_hamm.txt') as fp:
    for name, seq in read_fasta(fp):
        genes.append([name, seq])