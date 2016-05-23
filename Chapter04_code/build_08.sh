DBNAME=ch04
dropdb $DBNAME;
createdb -T template-v9 $DBNAME
~/odoo/odoo.py -d $DBNAME --addons-path=.,~/odoo/addons -i ch04_r08_computed

