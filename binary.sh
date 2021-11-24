#!/bin/bash
#convert an integer to its signed binary notation
number=$1
output=""
sign=""

#input error checking
[ -n $number ] && [ $number -eq $number ] 2>/dev/null || { echo "Please provide a valid integer an an argument" ; exit 1 ; }

#prepare the sign variable
[ $number -lt 0 ] && sign="0b1" && number=$(( number * -1 )) || sign="0b0"

#loop to produce binary notation
while (( $number > 0 )) ; do output="$(( $number % 2 ))${output}" ; number=$(( $number / 2 )) ; done

#sign and print binary notation
echo $sign${output}
