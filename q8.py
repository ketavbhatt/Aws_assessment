import pymysql
import config
import logging

# Logging config
logging.basicConfig(filename="q8_aws.log", format='%(asctime)s %(message)s', filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



connectn = pymysql.connect(host=config.host1, user=config.user1, password=config.pwd, db=config.db_name, port=config.port1)

# Cursor allows Python executable code in DB session 
cursr = connectn.cursor()


# Error handling for every operation
try:
    # Query String
    qry_create = "CREATE TABLE Songs(sid int, sname varchar(30))"

    # Query Execution
    cursr.execute(qry_create)

    # Listing Tables for viewing
    qry_show = "show tables"
    cursr.execute(qry_show)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as table is created successfully
    logging.info('Table Created')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e)
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_insert = "INSERT INTO Songs(sid, sname) VALUES (1, 'song1'),(2, 'song2'),(3, 'song3'),(4, 'song4')"

    # Query Execution
    cursr.execute(qry_insert)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is inserted successfully
    logging.info('Inserted Entries')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e)
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_read = "SELECT * FROM Songs"

    # Query Execution
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is queried successfully
    logging.info('Table Queried')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_update = "UPDATE Songs SET sid = 10, sname = 'movie9' WHERE sid = 1"
    qry_read = "SELECT * FROM Songs"
    
    # Query Execution 
    cursr.execute(qry_update)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is updated successfully
    logging.info('Table Updated')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')

try:
    # Query String
    qry_delete = "DELETE FROM Songs WHERE sid = 2"

    # Query Execution 
    cursr.execute(qry_delete)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is deleted successfully
    logging.info('Table Entry Deleted')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')


finally:
    # When all the queries are executed, commit all the changes
    connectn.commit()

    # CLose connection to RDS
    connectn.close()