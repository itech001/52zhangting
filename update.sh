
#get stock data
#python get_history.py > web/get_history.txt 2>&1

#generate pages
python gen_yaogu.py
python gen_yaogu2.py

#generate website
cd web2/
make publish
cp -rf ../web/* v1/

#submit
git add .
git commit -m "update"
git push
