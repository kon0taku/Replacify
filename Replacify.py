# Include standard modules
import argparse
import getopt, sys, re
from pathlib import Path


# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("-s", "--source", help="set the path to the source list")
parser.add_argument("-t", "--target", help="set the path to the target list")
parser.add_argument("-o", "--output", help="[OPTIONAL] set the output filename")
parser.add_argument("-w", "--word", help="set the word to replace in the target list")

# Read arguments from the command line
args = parser.parse_args()

quiteProgram= False

if args.source:
    src= Path(str(args.source))
else:
    print("You Must Provide A Source File")
    quiteProgram= True
if args.target:
    tgt= Path(str(args.target))
else:
    print("You Must Provide A Target File")
    quiteProgram= True
if args.word:
    wrd= str(args.word)
else:
    print("You Must Provide A Keyword")
    quiteProgram= True
if args.output:
    outputFlag= True
    outputFile= Path(str(args.output))
else:
    outputFlag= False


if quiteProgram== True:
    quit()


srcFile_Array = []
with open(src) as srcFile:
    for line in srcFile:
        srcFile_Array.append(line)



tgtFile_Array = []
with open(tgt) as tgtFile:
    for line in tgtFile:
        if wrd in line:
            tgtFile_Array.append(line.rstrip())
 


output_Array = []
for line in tgtFile_Array:
    for ln in srcFile_Array:
        output_Array.append(line.replace(str(wrd), str(ln).rstrip()))




if outputFlag== True:
    NewOutputFile = open(outputFile, "a")
   # NewOutputFile.write("\n")

    for l in output_Array:
        NewOutputFile.write(l)
        NewOutputFile.write("\n")

    NewOutputFile.close()

    print("Results output to %s" % args.output)

else:
    targetToAppendText = open(tgt, "a")
   # targetToAppendText.write("\n")

    for l in output_Array:
        targetToAppendText.write(l)
        targetToAppendText.write("\n")

    targetToAppendText.close()

    print("Results appended to %s" % args.target)
