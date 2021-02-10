import textwrap
import pyodbc
from flask import Flask,render_template, request

app = Flask(__name__)

# DataBase Connections

driver = '{ODBC Driver 17 for SQL Server}' 
server_name ='sample-web'
database_name ='sample-web'
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
username = "ramazdemo"
password = "Password123"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database_name+';UID='+username+';PWD='+ password)

# Code

@app.route('/', methods = ['GET','POST'])
def index():
    
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        crsr: pyodbc.Cursor = cnxn.cursor()
        crsr.execute("""INSERT INTO users (Name,Email) VALUES(?,?)""",(name,email))
        crsr.commit()
        crsr.close()
        return 'success'
    return render_template('index.html')
    #return """<form method="POST" action="">
    #                    <br />
    #                         <p> Welcome to Claim 360 </p>
    #                    <br />
    #                    <br> Member Name <input type="text" name="name" \> <br />
    #                    <br>
    #                        Member Email <input type="email" name="email" size="50" />
    #                    <br>
    #                    <br>
    #                                <input type="submit"/>
    #                    <br>
    #                    <br /> <button type="button">Get Users</button> <br />
    #            </form> """
if __name__ == '__main__':
    app.run(debug=True)
