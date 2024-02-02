from flask import Flask, render_template, request, redirect, url_for, flash
import cx_Oracle

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

con = cx_Oracle.connect("raviteja/raviteja@asus:1521/XE")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and "name" in request.form:
            details = request.form
            name = details['name']
            ssn = details['ssn']
            email = details['email']
            phone = details['phone']
            password = details['password']
            cur = con.cursor()
            cur.execute(f"""INSERT INTO register(name, ssn, email, phone, password) VALUES('{name}', '{ssn}','{email}', {phone}, '{password}')""")
            con.commit()
            flash('Registration Sucessfull!, Please LogIn', 'signup')
            
           
    if request.method == 'POST'and 's' in request.form:
            details = request.form
            ssn = details['s']
            password = details['p']
            cur = con.cursor()
            s = cur.execute(f"""select ssn, password from register""")
            m = dict(s)
            for i, j in m.items():
                if i == ssn:
                    if j == password:
                        
                        return redirect('/home')
            else:
                flash('Invalid SSN or Password, Please try again', 'login')
    return render_template('login.html')
      
@app.route('/home', methods=['GET', 'POST'])
def publisher():
    if request.method == 'POST' and "phone" in request.form:
        details = request.form
        name = details['name']
        address = details['address']
        phone = details['phone']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO publisher(name, address, phone) VALUES('{name}', '{address}', {phone})""")
        con.commit()
        flash('1 row inserted', 'publi')
        
    elif request.method == 'POST' and "br_address" in request.form:
        details = request.form
        br_id = details['br_id']
        br_name = details['br_name']
        br_address = details['br_address']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO library_branch(branch_id, branch_name, address) VALUES({br_id}, '{br_name}', '{br_address}')""")
        con.commit()
        flash('1 row inserted', 'br')
   
    elif request.method == 'POST' and "bo_title" in request.form:
        details = request.form
        bo_id = details['bo_id']
        bo_title = details['bo_title']
        pub_name = details['pub_name']
        pub_year = details['pub_year']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO book(book_id, title, publisher_name, pub_year) VALUES({bo_id}, '{bo_title}', '{pub_name}', {pub_year})""")
        con.commit()
        flash('1 row inserted', 'bo')
    
    elif request.method == 'POST' and "a_name" in request.form:
        details = request.form
        bo_id = details['bo_id']
        a_name = details['a_name']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO book_authors(book_id, author_name) VALUES({bo_id},'{a_name}')""")
        con.commit()
        flash('1 row inserted', 'ba')
    
    elif request.method == 'POST' and "no_name" in request.form:
        details = request.form
        bo_id = details['bo_id']
        br_id = details['br_id']
        no_name = details['no_name']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO book_copies(book_id, branch_id, no_copies) VALUES({bo_id},{br_id},{no_name})""")
        con.commit()
        flash('1 row inserted', 'bc')
        
    elif request.method == 'POST' and "due" in request.form:
        details = request.form
        bo_id = details['bo_id']
        br_id = details['br_id']
        card_no = details['card_no']
        date_o = details['date_o']
        due = details['due']
        cur = con.cursor()
        cur.execute(f"""INSERT INTO book_lending(book_id, branch_id, card_no, date_out, due_date) VALUES({bo_id},{br_id},{card_no},'{date_o}','{due}' )""")
        con.commit()
        flash('1 row inserted' , 'bl')

    return render_template('home.html')
	

