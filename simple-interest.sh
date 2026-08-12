#!/bin/bash
# Simple Interest Calculator Script

echo "Enter Principal Amount:"
read p
echo "Enter Rate of Interest per annum:"
read r
echo "Enter Time period in years:"
read t

# Calculating Simple Interest
s=`expr $p \* $t \* $r / 100`

echo "The Simple Interest is: $s"
