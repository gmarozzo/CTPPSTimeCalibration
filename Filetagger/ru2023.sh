#!/usr/bin/bash
cd /eos/cms/store/express/Run2023D/StreamALCAPPSExpress/ALCARECO/PPSCalMaxTracks-Express-v1/000/369/956/00000
OUTPUTFILE="/eos/user/g/gdamolin/PPS_timeCalibration/CTPPSTimeCalibration/Filetagger/SecondtryList.txt"
EXE="/eos/user/g/gdamolin/PPS_timeCalibration/CTPPSTimeCalibration/Filetagger/tag2023.exe"
pwd
echo "Reached eos directory, starting the loop"

for file in $(find ./ -maxdepth 1 -mindepth 1 -type f); do $EXE $file $OUTPUTFILE; done

echo "fiished"
cd -

