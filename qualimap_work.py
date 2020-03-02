#!/usr/bin/env python
import os
import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description="qualimap run pipeline ")
    parser.add_argument('--pipline_path', type=str, help='the project abspath')
    parser.add_argument('--bamlist', type=str, help='the bam list,the first column is bam path,the second column is samplename')
    parser.add_argument('--gtf', type=str, help='the exon gtf path')
    parser.add_argument('--outformat', type=str, help='the outformat',default="PDF")
    parser.add_argument('-p','--sequencing_protoco', type=str,help='Sequencing library protocol:strand-specific-forward,strand-specific-reverse or non-strand-specific')
    parser.add_argument('--outdir', type=str, help='the output dir')
    args = parser.parse_args()
    return args

def main(args):
    pipline_path=args.pipline_path    
    bamlist=args.bamlist
    outdir=args.outdir
    gtf=args.gtf
    outformat=args.outformat
    sequencing_protoco=args.sequencing_protoco
    all_bams=open(bamlist,"r").readlines()
    work_file=open(outdir+"/work.sh","w")
    work_file.writelines("cd %s \n" % outdir)
    for each in all_bams:
        bams_file_path=each.split("\t")[0].strip()
        sample_name=each.split("\t")[1].strip()
        if bams_file_path:
            work_file.writelines("mkdir %s \n" % sample_name) 
            work_file.writelines("%s rnaseq -bam %s -gtf %s  -outdir %s  -outformat %s -p %s \n" %(pipline_path,bams_file_path,gtf,outdir+"/"+sample_name,outformat,sequencing_protoco))   
        else:
            print("please check you bams path")

if __name__ == "__main__":
    args = arg_parser()
    main(args)
