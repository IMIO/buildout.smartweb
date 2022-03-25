for tbl in `psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -qAt -c "select tablename from pg_tables where schemaname = 'public';"` ; 
do 
  psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -c "drop table $tbl cascade" $YOUR_DB ; 
done
for tbl in `psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" $YOUR_DB` ; 
do
  psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -c "drop sequence $tbl" $YOUR_DB ;
done
for tbl in `psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -qAt -c "select table_name from information_schema.views where table_schema = 'public';" $YOUR_DB` ; 
do 
  psql -U $RELSTORAGE_USER -h $RELSTORAGE_HOSTNAME -p $RELSTORAGE_PORT -c "drop view $tbl" $YOUR_DB ; 
done
