from bottle import Bottle, route, run, template, request, response, static_file
import psycopg2
import os
app = Bottle()

conn = psycopg2.connect(database = "ddutsb1d2s65af", user = "jotkvsxdutmqyp", password = "813b3a1e52dcbaa8b9aac865e0324ae1cfd662b86d5a846e2b2d0e3f37cbe0d5", host = "ec2-35-175-155-248.compute-1.amazonaws.com", port = "5432")
conn.set_session(autocommit=True)
cur = conn.cursor()

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    # response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/')
def index():
	if request.method == 'OPTIONS':
		return {}
	return static_file('index.html', root='./dist')

@app.route('/js/<filename>')
def static_js(filename):
	return static_file(filename, root='./dist/js')

@app.route('/css/<filename>')
def static_css(filename):
	return static_file(filename, root='./dist/css')

@app.route('/img/<filename>')
def static_img(filename):
	return static_file(filename, root='./dist/img')

@app.route('/getuser', method=['GET', 'OPTIONS'])
def getuser():
	if request.method == 'OPTIONS':
		return {}
	user_id = request.query.user_id
	print(user_id)
	cur.execute('''select name from fin.USER where user_id=%s;''', (user_id,))
	results = cur.fetchall()

	all_names = []
	for result in results:
		all_names.append(result[0])

	return {"all_names": all_names}

@app.route('/gettodos', method=['GET', 'OPTIONS'])
def gettodos():
	if request.method == 'OPTIONS':
		return {}
	completed = request.query.completed

	completed = parse_bool(completed)

	where_clause = " where completed=%s"

	santa_clause = "select todo_id, description, due_date, completed from fin.todos"

	query = ""
	params = ()

	if completed is True:
		query = santa_clause + ";"
	else:
		query = santa_clause + where_clause + ";"
		params = (completed,)
	
	cur.execute(query,params)
	results = cur.fetchall()

	all_todos = []
	for result in results:
		all_todos.append({"id": result[0], "title": result[1],"due_date":str(result[2]),"completed":result[3]})


	return {"all_todos":all_todos}

# @app.route('/fetchtodos', method=['GET', 'OPTIONS'])
# def fetchtodos():
# 	if request.method == 'OPTIONS':
# 		return {}
	
# 	cur.execute('''select todo_id, description, due_date, completed from fin.todos;''')
# 	results = cur.fetchall()

# 	all_todos = []
# 	for result in results:
# 		all_todos.append({"id": result[0], "title": result[1],"due_date":str(result[2]),"completed":result[3]})

# 	return {"all_todos":all_todos}

@app.route('/newtodo', method = ['POST', 'OPTIONS'])
def newtodo():
	if request.method == 'OPTIONS':
		return {}
	todo_description = request.json.get('description')
	due_date = request.json.get('due_date')


	cur.execute('''insert into fin.todos (description, due_date) values (%s,%s) returning todo_id;''', (todo_description, due_date))
	new_todo_id = cur.fetchone()

	return {"id": new_todo_id[0], "title": todo_description, "due_date": due_date}

@app.route('/update_todo', method = ['POST', 'OPTIONS'])
def update():
	if request.method == 'OPTIONS':
		return {}
	new_todo_description = request.json.get('description')
	todo_id = request.json.get('todo_id')

	#fetch the old description
	cur.execute('''select description from fin.todos where todo_id=%s;''',(todo_id,))
	old_description = cur.fetchone()

	#update the description
	cur.execute('''update fin.todos set description = %s where todo_id = %s;''', (new_todo_description, todo_id))
	

	return {"todo_id":todo_id, "new_description": new_todo_description, "old_description": old_description[0]}

@app.route('/toggle_todo', method = ['POST', 'OPTIONS'])
def toggle():
	if request.method == 'OPTIONS':
		return {}
	todo_id = request.json.get('todo_id')

	cur.execute('''update fin.todos set completed = not completed where todo_id = %s returning completed;''', (todo_id,))
	comp_status = cur.fetchone()

	return{"comp_status":comp_status}


@app.route('/delete', method = ['POST', 'OPTIONS'])
def delete_todo():
	if request.method == 'OPTIONS':
		return {}
	todo_id = request.json.get('todo_id')

	#delete the todo with the given todo_id
	cur.execute('''delete from fin.todos where todo_id = %s;''', (todo_id,))

def parse_bool(s):
	return s.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

run(app, host = '0.0.0.0', port = int(os.environ.get("PORT",8080)), debug = True)