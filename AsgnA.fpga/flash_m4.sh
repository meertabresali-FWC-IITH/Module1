#!/bin/bash

ql_symbiflow -compile -src /data/data/com.termux/files/home/fpga-examples/blink -d ql-eos-s3 -P PU64 -v helloworldfpga.v -t helloworldfpga -p quickfeather.pcf -dump binary


pdflatex helloworldfpga.tex

zathura helloworldfpga.pdf

#termux-open arm.tex
