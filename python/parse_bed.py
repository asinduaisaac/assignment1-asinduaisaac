#The program requesting from the bed file from the user
#for each chromosome calculate the number of reads 
# calculate the average read quality
#load the menu DONE
#Select an option
  #[R] Display read counts in each Chromosome
  #[D] Display the average read quality for each chromosome
  #[X] Exit
  
  #below is the logic for the program me
  
def get_chr_sort_key(chrom):
    # turns "chr1", "chr10", "chrX" into something we can sort properly
    # (plain text sorting would put chr10 before chr2, which is wrong)
    name = chrom.replace("chr", "")
    if name.isdigit():
        return (0, int(name))
    else:
        return (1, name)

#add a comment
counts={}
total_read_quality={}

bed_file=input("Please enter the name of the bed file: ")

working_bedfile = open(bed_file ,"r")


for line in working_bedfile:
    line=line.strip()
    
    if not line or line.startswith("#"): 
        continue
    
    columns=line.split()
    
    chromosome=columns[0]
    read_quality = float(columns[3])
    if chromosome not in counts: 
        counts[chromosome]=1
        total_read_quality[chromosome] =  read_quality
        
    else:
        counts[chromosome] = counts[chromosome]+1 
        
        total_read_quality[chromosome] = total_read_quality[chromosome] + read_quality

    
working_bedfile.close() 
  
  
  
while True: 
    print("Select an option")
    print("[R] Display read counts in each Chromosome")
    print("[D] Display the average read quality for each chromosome")
    print("[X] Exit")
    option=input("Please select an option from the menu: ").upper()
    if option=="R":
        # natural order first (chr1, chr2, chr3... chrX, chrY) - this is what the spec example shows
        natural_order_chromosomes = sorted(counts, key=get_chr_sort_key)
        
        chr_heading="Chr "
        count_heading="count"
        output=f"{chr_heading}    {count_heading}\n"
        
        for each_chromosome in natural_order_chromosomes:
            output = output + f"{each_chromosome}    {str(counts[each_chromosome])}\n"
        
        output_file = open("./read_counts.txt", "w")  
        output_file.write(output)
        output_file.close()
        
        print(output)
        
        # bonus: same counts, but ordered by read count, descending
        sorted_chromosomes = sorted(counts,key=lambda chr:counts[chr], reverse=True)
        bonus_output = "\nBonus - ordered by read count (descending):\n"
        for each_chromosome in sorted_chromosomes:
            bonus_output = bonus_output + f"{each_chromosome}    {str(counts[each_chromosome])}\n"
        
        print(bonus_output)
        
        
    elif option=="D":
        natural_order_chromosomes = sorted(counts, key=get_chr_sort_key)
        
        output = ""
        for chromosome in natural_order_chromosomes:
           average = total_read_quality[chromosome]/counts[chromosome]
           output = output + f"{chromosome}   {average:.3f}\n"
           
        print(output)
        
        output_file = open("./average_counts.txt", "w")  
        output_file.write(output)
        output_file.close()
        
    elif option=="X":
        print("You have exited the program")  
        break   
    else:
        print("Invalid option, please select a valid option from the menu")
