#/bin/bash
if [ -z "$1" ];
then
    echo "Provide test selection - public or private"
    exit 1
fi

if [ "$1" != "public" ] && [ "$1" != "private" ];
then
    echo "Only possible selections are public or private"
    exit 1
fi

if [ "$1" == "public" ];
then
    tests=10
else
    tests=100
fi

ROOT=$PWD

cd testcases
START=$PWD

for problem in ./*/;
do
 echo "Generating $tests tests for problem $problem"
#  if [ $problem != "./beautiful-towers-i/" ] ;
#  then continue
#  fi
 cd $problem/
 rm -rf outputs
 mkdir outputs
 python fuzzer.py
 public_tests=$(find ./outputs | shuf -n $tests)
 for submission in $ROOT/$problem/*/;
 do
    #echo $submission
    file=$(ls $submission | grep wrong)
    file=${file%%.py}
    
    #echo $private_tests > $submission/private_tests
    #echo $public_tests > $submission/public_tests

    rm $submission/${1}_new*.py
    for test in $public_tests ;
    do
        cp $test $submission/${1}_$(basename $test)
        sed -i "1s/^/from $file import *\n/" $submission/${1}_$(basename $test)
    done
 done
 cd $START
done