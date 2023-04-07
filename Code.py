

import random
import csv
import matplotlib.pyplot as plt
import pandas as pd
# Define the number of genes to generate
num_genes = 100

# Define the chromosome numbers to use
chromosomes = list(range(1, 11))

# Define the minimum and maximum SNP numbers for each gene
min_snp = 100
max_snp = 1000

# Define the length of each chromosome
chromosome_lengths = {
    1: 37718439,
    2: 31611734,
    3: 40564783,
    4: 26049113,
    5: 45217253,
    6: 54099293,
    7: 22766400,
    8: 29265719,
    9: 62871001,
    10: 15338199
}

# Generate random genes and write to CSV file
with open('random_genes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'chromosome', 'start', 'end', 'number'])

    for i in range(num_genes):
        name = 'Gene{}'.format(i+1)
        chromosome = random.choice(chromosomes)
        start = random.randint(1, chromosome_lengths[chromosome])
        end = random.randint(start, chromosome_lengths[chromosome])
        snps = random.randint(min_snp, max_snp)

        writer.writerow([name, chromosome, start, end, snps])

# Read data from CSV file
df = pd.read_csv('random_genes.csv')

# Set up figure and subplots
fig, axs = plt.subplots(2, 5, figsize=(15, 6), sharex=True, sharey=True)

# Define colors for each chromosome
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# Create stacked line chart for each chromosome subplot
for i in range(10):
    ax = axs[i//5, i%5]
    data = df[df['chromosome']==i+1]
    data = data.sort_values('start')
    ax.stackplot(data['start'], data['number'], colors=colors[i])
    ax.set_title('Chromosome {}'.format(i+1))
    ax.set_xlabel('Position')
    ax.set_ylabel('Number of SNPs')

# Add overall title and adjust spacing
fig.suptitle('SNP Distribution by Chromosome', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
