#!/bin/sh -x

export PATH=/usr/local/bin:$PATH

dir=`dirname $0`
cd $dir

for arg in "$@"
do
  if [ "$arg" = "-history" ]
  then
    history=yes
  fi
  if [ "$arg" = "-pull_code" ]
  then
    pull_code=yes
  fi
  if [ "$arg" = "-push_code" ]
  then
    push_code=yes
  fi
  if [ "$arg" = "-deploy" ]
  then
    deploy=yes
  fi
done

echo pull code
if [ "$pull_code" = "yes" ]
then
  git reset --hard
  git pull
fi

echo get stock data and insert into db
if [ "$history" = "yes" ]
then
   #python3 get_history.py
   python3 get_latest_sina.py
fi

echo generate pages
#python3 gen_yaogu.py
python3 gen_yaogu2.py
python3 gen_qushi.py
python3 gen_zuori.py
python3 gen_dadie.py
echo call pelican
cd web2/
make publish
cd ../

d=`date "+%Y-%m-%d"`
echo push code
if [ "$push_code" = "yes" ]
then
    git add .
    git commit -m $d
    git push
fi

echo deploy
if [ "$deploy" = "yes" ]
then
    cp -rf web2/output/* /var/www/52zhangting/
fi

exit 0
