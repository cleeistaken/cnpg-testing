TEST_CASES=(3 6 12 24 48 96)

for item in "${TEST_CASES[@]}"; do
  echo "RUNNING TEST CASE $item"
  echo "======================================================"
  export TMP=`pwd`/TMP
  mkdir -p $TMP
  echo "BUILD HAMMERDB SCHEMA"
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  VU=$item ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_buildschema.py
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  echo "CHECK HAMMERDB SCHEMA"
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_checkschema.py
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  echo "RUN HAMMERDB TEST"
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_run.py
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  echo "DROP HAMMERDB SCHEMA"
  ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_deleteschema.py
  echo "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
  echo "HAMMERDB RESULT"
  ./hammerdbcli py auto ./scripts/python/postgres/tprocc/pg_tprocc_result.py
done