#!/bin/tclsh
# maintainer: Pooja Jain
import os

print("Get Parameters")
VU_ARG = os.getenv('VU')
if not VU_ARG:
    print("Using default number of CPU")
    vu = tclpy.eval('numberOfCPUs')
else:
    vu = int(VU_ARG)

print(f"Using {vu} vCPU <--------------------------------------------------------------------------")

print("SETTING CONFIGURATION")
dbset('db','pg')
dbset('bm','TPC-C')

diset('connection','pg_host','cnpg-postgres-cluster-rw')
diset('connection','pg_port','5432')
diset('connection','pg_sslmode','prefer')

warehouse = int(vu) * 5
diset('tpcc','pg_count_ware',warehouse)
diset('tpcc','pg_num_vu',vu)
diset('tpcc','pg_superuser','postgres')
diset('tpcc','pg_superuserpass','postgres')
diset('tpcc','pg_defaultdbase',' postgres')
diset('tpcc','pg_user','tpcc')
diset('tpcc','pg_pass','tpcc')
diset('tpcc','pg_dbase','tpcc')
diset('tpcc','pg_tspace','pg_default')
if (warehouse >= 200): 
    diset('tpcc','pg_partition','true') 
else:
    diset('tpcc','pg_partition','false') 

print("SCHEMA BUILD STARTED")
buildschema()
print("SCHEMA BUILD COMPLETED")
exit()
