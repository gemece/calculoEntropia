#!/usr/bin/python
#
# graph_file_entropy.py 
# 
# Shannon Entropy of a file 
# = minimum average number of bits per character 
# required for encoding (compressing) the file 
# 
# So the theoretical limit (in bytes) for data compression: 
# Shannon Entropy of the file * file size (in bytes) / 8 
# (Assuming the file is a string of byte-size (UTF-8?) characters 
# because if not then the Shannon Entropy value would be different.) 
# FB - 201011291 
import sys 
import math 

if len(sys.argv) != 2: 
    print "Usage: ", sys.arv[0], " [path]filename" 
    sys.exit()

# read the whole file into a byte array
f = open(sys.argv[1], "rb") 
fBytes = map(ord, f.read()) 
f.close() 
fSize = len(fBytes) 


# calculate the frequency of each byte value in the file 
# and use map to get the Histogram (Normalized to unit area)
bCount=[0 for a in range(256)]
for bval in fBytes: 
    bCount[bval] += 1
bHisto=map(lambda x: float(x)/fSize, bCount)


# calculate the average value of byte for the file
avByte=float(0)
bValue=[a for a in range(256)]
for bval in bValue: 
    avByte = avByte + float(bval) * bCount[bval]
avByte = avByte / fSize

eVector=map(lambda x: float(x)*math.log(x, 2), filter(lambda x: x>0, bHisto))
enValue= -reduce( (lambda x,y: x+y), eVector)
mfSizeb=(enValue * fSize)
mfSizeB=mfSizeb/8

print "# File ____________________: ", sys.argv[1]
print "# File size _______________: ", fSize, " bytes."
print "# Average byte value ______: ", avByte
print "# Entropy (min bits/byte) _: ", enValue
print "# Min possible filesize ___: ", mfSizeb, "bits, ", mfSizeB, "bytes."
