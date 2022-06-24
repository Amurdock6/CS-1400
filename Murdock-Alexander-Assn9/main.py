# Alexander Murdock
# CS-1400-002

class Genome:
    def __init__(self, genome):
        self.genome = genome
    
    def geneGroomer(self, genome):
        genome = genome.upper()
    
        i = 0
        while i < len(genome):
            if genome[i] != 'A' and genome[i] != 'C' and genome[i] != 'T' and genome[i] != 'G':
                genome = genome[:i] + genome[i + 1:]
            else:
                i += 1
        return genome
    
    
    def genomeSlash(self, genome):
        genome = self.geneGroomer(genome)
        
        startMarker = "ATG"
    
        startIndex = genome.find(startMarker)
    
        # if I can't find the startMarker at all
        # there is no gene, and I return "no gene is found"
        if startIndex == -1:
            print("no gene is found")
            return "", ""
    
        # I did find a startMarker
        genome = genome[startIndex + len(startMarker):]
    
        # look for another startMarker
        startIndex = genome.find(startMarker)
    
        # if I can't find the startMarker in what is left
        # there is only one gene possible
        if startIndex == -1:
            return genome, ""
    
        # if there is another startMarker, split the first gene off
        gene = genome[:startIndex]
        genome = genome[startIndex:]
        return gene, genome
    
    def geneSnip(self, gene):
        # possible end markers:  TAG, TAA, TGA
        TagIndex = gene.find("TAG")
        TaaIndex = gene.find("TAA")
        TgaIndex = gene.find("TGA")
    
        if TagIndex == -1 and TaaIndex == -1 and TgaIndex == -1:
            return gene
    
        if TagIndex != -1: gene = gene[:TagIndex]
        if TaaIndex != -1: gene = gene[:TaaIndex]
        if TgaIndex != -1: gene = gene[:TgaIndex]
        return gene
    
    def display(self):
        genome = self.genome.upper()
    
        print(self.geneGroomer(genome))
    
    def genes(self):
        genome = self.genome.upper()
    
        while genome != "":
            gene, genome = self.genomeSlash(genome)
            gene = self.geneSnip(gene)

            # Checks to make sure gene is long enough to actually be a gene
            if len(gene) >= 3:
                print(gene)
        

# write your class code above this line
# make no changes below this line


def main():

    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
