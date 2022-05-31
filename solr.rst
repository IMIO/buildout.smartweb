Documentation for SolR management
=================================

Initialize local cluster base config
------------------------------------
docker exec -ti solr1 bash -c "cd /solr-config && /opt/solr/bin/solr create_collection -c news -d news"
docker exec -ti solr1 bash -c "cd /solr-config && /opt/solr/bin/solr create_collection -c web -d web"
docker exec -ti solr2 bash -c "cd /solr-config && /opt/solr/bin/solr create_collection -c smartweb_test -d web"
docker exec -ti solr2 bash -c "cd /solr-config && /opt/solr/bin/solr create_collection -c events -d events"
docker exec -ti solr3 bash -c "cd /solr-config && /opt/solr/bin/solr create_collection -c directory -d directory"


Get collections
---------------

curl -X GET http://localhost:8983/solr/admin/collections?action=LIST


Get a collection schema
-----------------------

curl -X GET http://localhost:8983/solr/{core}/schema?wt=schema.xml

Example :
curl -X GET http://localhost:8983/solr/news/schema?wt=schema.xml


Update a collection schema
--------------------------

Update a collection
docker exec -ti solr1 bash -c "cd /solr-config && /opt/solr/bin/solr zk upconfig -d web -n web"
docker exec -ti solr1 bash -c "cd /solr-config && /opt/solr/bin/solr zk upconfig -d web -n smartweb_test"
