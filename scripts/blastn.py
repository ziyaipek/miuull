import snakemake
from snakemake.shell import shell

query = snakemake.input.query
out = snakemake.output[8]

db_prefix = snakemake.params.db_prefix
perc_identity = snakemake.params.perc_identity
outfmt = snakemake.params.outfmt
num_threads = snakemake.params.num_threads
max_target_seqs = snakemake.params.max_target_seqs
max_hsps = snakemake.params.max_hsps

shell(f"""
    blastn -query {query} -db {db_prefix} -out {out} \
    -perc_identity {perc_identity} \
    -outfmt {outfmt} \
    -num_threads {num_threads} \
    -max_target_seqs {max_target_seqs} \
    -max_hsps {max_hsps}
""")