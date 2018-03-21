# Function shows an example of connecting to MSSQL Server with Python.
# Includes an edge case of the sql variable being a table name.
# Includes writing results to a csv file.

import os
import csv
import pyodbc

def querydata(tblname):
    """ Connect to MSSQL and pull all data in a table.  Case illustrates
        limits of bound parameters.  Table name does not take the ? as a
        bound parameter.  The solution below is vulnerable to SQL injection, 
        but T-SQL does not allow binding a table name as a variable when 
        passing to the EXEC command.  
        Use something like:
        'SELECT user FROM tblx WHERE userid = ?' when needing a variable in a 
        SQL statement to avoid SQL injection.  The bind operator does not work 
        with table names."""
        
    connection_str ="""
      Driver={SQL Server};
      Server=SERVERNAME;
      Database=DB;
      Trusted_Connection=yes;
      """
    conn = pyodbc.connect(connection_str)
    cur = conn.cursor()

    sql = 'SELECT * FROM {table_name};'.format(table_name=tblname)

    rows = cur.execute(sql)
    # Example of writing the results to a file if results not too large.
    fname = ('{0}{1}'.format(tblname, '.txt'))
    path = os.path.join('C:\\', 'path', 'to', 'file', fname)

    with open(path, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow([x[0] for x in cur.description])         
        for row in rows:
            writer.writerow(row)
            
    return fout            