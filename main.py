import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

blast_G_muris = pd.read_csv("/home/hypnex/PycharmProjects/miuull/output/blastn/G_intestinalis/G_muris.blastn", sep="t", header=None)
blast_S_salmonicida = pd.read_csv("/home/hypnex/PycharmProjects/miuull/output/blastn/G_intestinalis/S_salmonicida.blastn", sep="t", header=None)

blast_G_muris.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
blast_S_salmonicida.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

num_hits_blast_G_muris = len(blast_G_muris)
num_hits_blast_S_salmonicida = len(blast_S_salmonicida)

print("Number of hit for Giardia intestinalis vs. Giardia muris: ", num_hits_blast_G_muris)
print("Number of hit for Giardia intestinalis vs. Spironucleus salmonicida: ", num_hits_blast_S_salmonicida)

sns.histplot(data=blast_G_muris, x='pident')

pivot_table = pd.pivot_table(blast_G_muris, values='length', index='qseqid', columns='sseqid')
sns.heatmap(pivot_table)

sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='bitscore', hue='pident')

sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='length', hue='pident')