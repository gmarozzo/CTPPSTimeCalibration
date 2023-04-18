#!/usr/bin/bash
cd /eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C
OUTPUTFILE="/afs/cern.ch/user/g/gdamolin/CMSSW_12_6_4/src/CTPPSTimeCalibration/Filetagger/ListLowPUFiles.txt"
EXE="/afs/cern.ch/user/g/gdamolin/CMSSW_12_6_4/src/CTPPSTimeCalibration/Filetagger/test.exe"
pwd
echo "Reached eos directory, starting the loop"

#for file in $(find ./ -maxdepth 5 -mindepth 5 -type f); do $EXE $file $OUTPUTFILE; done

for file in $(find ./EphemeralZeroBias0/EphemeralZeroBias0/220906_135809/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "1"
for file in $(find ./EphemeralZeroBias1/EphemeralZeroBias1/220906_135833/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "2"
for file in $(find ./EphemeralZeroBias2/EphemeralZeroBias2/220906_135858/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "3"
for file in $(find ./EphemeralZeroBias3/EphemeralZeroBias3/220906_135923/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "4"
for file in $(find ./EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "5"
for file in $(find ./EphemeralZeroBias5/EphemeralZeroBias5/220906_140025/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "6"
for file in $(find ./EphemeralZeroBias6/EphemeralZeroBias6/220906_140052/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "7"
for file in $(find ./EphemeralZeroBias7/EphemeralZeroBias7/220906_102839/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "8"
for file in $(find ./EphemeralZeroBias8/EphemeralZeroBias8/220906_140118/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "9"
for file in $(find ./EphemeralZeroBias9/EphemeralZeroBias9/220906_140143/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "10"
for file in $(find ./EphemeralZeroBias10/EphemeralZeroBias10/220906_140208/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "11"
for file in $(find ./EphemeralZeroBias11/EphemeralZeroBias11/220906_140233/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "12"
for file in $(find ./EphemeralZeroBias12/EphemeralZeroBias12/220906_140258/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "13"
for file in $(find ./EphemeralZeroBias13/EphemeralZeroBias13/220906_140322/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "14"
for file in $(find ./EphemeralZeroBias14/EphemeralZeroBias14/220906_140346/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "15"
for file in $(find ./EphemeralZeroBias15/EphemeralZeroBias15/220906_140416/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "16"
for file in $(find ./EphemeralZeroBias16/EphemeralZeroBias16/220906_140447/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "17"
for file in $(find ./EphemeralZeroBias17/EphemeralZeroBias17/220906_140513/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "18"
for file in $(find ./EphemeralZeroBias18/EphemeralZeroBias18/220906_140545/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "19"
for file in $(find ./EphemeralZeroBias19/EphemeralZeroBias19/220906_140617/0000 -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done
echo "20, done!"



