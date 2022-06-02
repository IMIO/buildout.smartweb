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


Warnings
--------

Some changes need a restart of SolR :
- Adapting filters in field types
- Adapting synonyms (synonyms.txt file)


Fuzzy search
------------

A fuzzy search can be used to have a spellcheck. The fuzzy search use Damerau-Levenshtein Distance.
To make a fuzzy search just add "~" at the end of the searched term(s).

An optional distance parameter specifies the maximum number of edits allowed, between 0 and 2, defaulting to 2. For example:

test~2

More documentation : https://solr.apache.org/guide/8_10/the-standard-query-parser.html#fuzzy-searches
