#!/bin/sh -x
for arg in "$@"
do
  if [ "$arg" = "-history" ]
  then
    history=yes
  fi
done

#get stock data
if [ "$history" = "yes" ]
then
   echo get history
   python get_history.py
   #python get_history.py > web/get_history.txt 2>&1
fi

echo generate pages
python gen_yaogu.py
python gen_yaogu2.py
python gen_qushi.py

echo generate website
cd web2/
make publish
#cp output/others/404.html output/
mkdir output/v1
cp -rf ../web/* output/v1/
cd ../

#submit
#git add .
#git commit -m "update"
#git push
