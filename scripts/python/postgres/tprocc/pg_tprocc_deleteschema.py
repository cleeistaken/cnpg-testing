#!/bin/tclsh
# maintainer: Pooja Jain

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host','cluster-sample-rw')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass','wcOJ4Te29iuTYcgv2gYXGHDo08GlWJmySjZIoQxsBY1C7Cdx9bBEBxMoJgmyGTj4')
diset('tpcc','pg_defaultdbase','postgres')
diset('tpcc','pg_user','tpcc')
diset('tpcc','pg_pass','tpcc')
diset('tpcc','pg_dbase','tpcc')

print("DROP SCHEMA STARTED")
deleteschema()
print("DROP SCHEMA COMPLETED")
exit()
