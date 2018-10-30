import sqlite3
from pandas import read_sql_query

con = sqlite3.connect("chinook.db")

def query(query_string, print_df=True):
    df = read_sql_query(query_string, con)
    if print_df: print df
    return df

# Question 1: How many employees?

def q1():
    query('SELECT * FROM employees;')
    query('SELECT DISTINCT COUNT(EmployeeId) as Num FROM employees;')

# Question 2: How many customers named Richard?

def q2():
    query('SELECT * FROM customers;')
    query('''
        SELECT
            DISTINCT COUNT(CustomerId) as Num 
        FROM
            customers
        WHERE
            FirstName="Richard";
        ''')

# Question 3: Which employees helped customers named Ed or some version of Ed?

def q3():
    query('''
        SELECT 
            e.FirstName AS rep_name, 
            c.FirstName as customer_name
        FROM
            customers AS c
        JOIN
            employees AS e
        ON
            (c.SupportRepId=e.EmployeeId)
        WHERE
            c.FirstName LIKE "Ed%";
        ''')

# Question 4: Find all employees who were not matched with customers

def q4():
    query('''
        SELECT DISTINCT
            e.EmployeeId AS id,
            e.FirstName AS free_rep
        FROM
            employees AS e
        LEFT JOIN
            customers AS c
        ON
            (c.SupportRepId=e.EmployeeId)
        WHERE
            c.SupportRepId IS NULL;
        ''')

# Question 5: Find all genres

def q5():
    query('''
        SELECT DISTINCT
            Name
        FROM
            genres;
        ''')

# Question 6: Find song length by genre

def q6():
    query('''
        SELECT
            g.Name AS genre,
            ROUND(AVG(t.Milliseconds)/60000.0, 3) AS avglength_min
        FROM
            tracks as t
        JOIN
            genres as g
        USING
            (GenreId)
        GROUP BY
            g.Name
        ORDER BY
            g.Name;
        ''')

# Question 7: Find which tracks were the most expensive

def q7():
    query('''
        SELECT
            Name AS name,
            UnitPrice AS price
        FROM
            tracks
        ORDER BY
            UnitPrice DESC;
        ''')

# Question 8: Find which GENRES were the most expensive

def q8():
    query('''
        SELECT
            g.Name AS genre,
            AVG(t.UnitPrice) AS avgprice_dollars
        FROM
            genres AS g
        JOIN
            tracks as t
        USING
            (GenreId)
        GROUP BY
            g.GenreId
        ORDER BY
            AVG(t.UnitPrice) DESC;
        ''')

# Question 9: What playlists contain the most songs?

def q9():
    # there were some dup values of playlistId / playlist tracks here.
    query('''
        SELECT DISTINCT
            p.Name as playlist,
            COUNT(t.TrackId) AS num_songs
        FROM
            playlists AS p
        JOIN
            playlist_track AS pt
        USING
            (PlaylistId)
        JOIN
            tracks AS t
        USING
            (TrackId)
        GROUP BY
            p.PlaylistId
        ORDER BY
            COUNT(t.TrackId) DESC;
        ''')

# Question 10: Which customers on average pay the most?

def q10():
    query('''
        SELECT DISTINCT
            c.FirstName AS customer,
            SUM(i.Total) AS totpay
        FROM
            customers AS c
        LEFT JOIN
            invoices AS i
        USING
            (CustomerId)
        GROUP BY
            c.CustomerId
        ORDER BY
            SUM(i.Total) DESC;
        ''')

# Question 11: What is the most common genre that each customer purchases?

def q11():
    query('''
        SELECT
            FirstName,
            LastName,
            Genre,
            MAX(Freq) AS Freq
        FROM
            (SELECT
                c.FirstName AS FirstName,
                c.LastName AS LastName,
                c.CustomerId AS CID,
                g.Name AS Genre,
                COUNT(g.GenreId) AS Freq
            FROM
                customers AS c
            JOIN
                invoices AS i
            USING
                (CustomerId)
            JOIN
                invoice_items AS it
            USING
                (InvoiceId)
            JOIN
                tracks AS t
            USING
                (TrackId)
            JOIN
                genres as g
            USING
                (GenreId)
            GROUP BY
                CID,
                g.GenreId)
        GROUP BY
            CID
        ORDER BY
            Freq DESC,
            FirstName ASC;
        ''')

# Question 12: Which employees have helped the most people?

def q12():
    query('''
        SELECT
            e.FirstName AS FirstName,
            e.LastName AS LastName,
            COUNT(c.CustomerId) AS NumCustomers
        FROM
            employees AS e
        LEFT JOIN
            customers AS c
        ON
            (e.EmployeeId=c.SupportRepId)
        GROUP BY
            e.EmployeeId
        ORDER BY
            NumCustomers DESC;
        ''')

if __name__ == "__main__":
    q12()
    pass

con.close()