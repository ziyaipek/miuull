rule all:
    input: "output/tRNA_scan_result.txt",
           "output/G_intestinalis.tRNA",
            expand("output/tRNAscan/{sp}.tRNA", sp=["G_muris","G_intestinalis"]),
            expand("output/blastn/G_intestinalis/{sp}.blastn", sp=["G_muris", "S_salmonicida"])

rule tRNAscan:
    input: "resource/G_intestinalis.fasta"
    output: "output/tRNA_scan_result.txt"
    shell: """tRNAscan-SE {input} -o {output} """

rule tRNAscan_stats:
    input:
            genome = "resource/G_intestinalis.fasta"
    output:
            tRNA = "output/G_intestinalis.tRNA",
            stats = "output/G_intestinalis.stats"
    params:
        threads = 2
    conda:
        "env/env.yaml"
    script:
        "scripts/tRNAscan_stats.py"

rule tRNAscan_stats_wildcard:
    input:
        genome = "resource/genomes/{genome}.fasta"
    output:
        tRNA = "output/tRNAscan/{genome}.tRNA",
        stats = "output/tRNAscan/{genome}.stats"
    params:
        threads = 2
    conda:
        "env/env.yaml"
    script:
        "scripts/tRNAscan_stats.py"

rule makeblastdb:
    input:
        "resources/{type}/db/{db}.fasta"
    output:
        multiext("output/{type}/db/{db}",
            ".ndb",
            ".nhr",
            ".nin",
            ".not",
            ".nsq",
            ".ntf",
            ".nto")
    params:
        outname="output/{type}/db/{db}"
    conda:
        "env/env.yaml"
    shell:
        'makeblastdb -dbtype nucl -in {input} -out {params.outname}'

rule blastn:
    input:
        query = "resources/{type}/query/{query}.fasta",
        db = "output/{type}/db/{db}.ndb"
    output:
        "output/{type}/{db}/{query}.blastn"
    params:
        perc_identity=95,
        outfmt=6,
        num_threads=2,
        max_target_seqs=1,
        max_hsps=1,
        db_prefix="output/{type}/db/{db}"
    conda:
        "env/env.yaml"
    script:
        "scripts/blastn.py"