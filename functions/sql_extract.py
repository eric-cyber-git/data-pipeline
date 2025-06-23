import pyodbc


def fetch_new_logs(checkpoint):
    """Fetch all logs with log_id greater than the provided checkpoint."""
    query = f'SELECT * FROM dbo.web_application WHERE log_id > {checkpoint};'
    return DB_Execute(query)
    
def fetch_ip_counts():
    """Aggregate IP address counts from the log table."""
    query = 'SELECT ip_address, COUNT(*) as hit_count FROM web_application GROUP BY ip_address'
    return DB_Execute(query)
    


def DB_Execute(passed_query):
    """Executes a SELECT statement and returns the result as a list of dictionaries."""
    
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Github_db;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
    cursor = conn.cursor()
    cursor.execute(passed_query)
    rows = cursor.fetchall()
    return rows_to_dict(cursor, rows)



def rows_to_dict(cursor, rows):
    """Convert pyodbc rows into a list of dictionaries using column headers."""
    columns = [col[0] for col in cursor.description]   
    return [dict(zip(columns, row)) for row in rows]
    

