import psycopg2

conn = psycopg2.connect(
        user="postgres",
        password="1234",
        host="localhost",
        port="5432",
        database="Form Submissions"  
    )
print("Database connection successful!")

    
curr = conn.cursor()

# SQL query to create the table
create_table_query = '''
CREATE TABLE FormSubmissions (
        ID SERIAL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        PhoneNumber VARCHAR(15),
        EmailAddress VARCHAR(100)
    );
    '''
    

curr.execute(create_table_query)
conn.commit()  

print("Table 'FormSubmissions' created successfully!")

 
curr.close()
conn.close()

print(f"Error: {e}")
