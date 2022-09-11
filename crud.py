from flask import Flask, request , jsonify

app=Flask(__name__)
course_list=[
    {
        "id":1,
        "name":"C Language",
        "fee":"1000",
    },
    {
        "id":2,
        "name":"C++ Language",
        "fee":"1000",
    },
    {
        "id":3,
        "name":"Java Programming",
        "fee":"1500",
    }
    
]

@app.route('/c',methods=['GET','POST'])
def courses():
    if request.method == 'GET':
        if len(course_list)>0:
            return jsonify(course_list)
        else:
            'Nothing Found'
            
    if request.method == 'POST':
        new_name=request.form['name']
        new_fee=request.form['fee']
        new_id=course_list[-1]['id']+1
        
        new_obj={
            'id':new_id,
            'name':new_name,
            'fee':new_fee
        }
        course_list.append(new_obj)
        return jsonify(course_list),201
    
    

@app.route('/ce/<int:id>',methods=['GET','PUT','DELETE'])
def single_course(id):
    if request.method=='GET':
        for course in course_list:
            if course['id']==id:
                return jsonify(course)
            pass
    
    if request.method=='PUT':
        for course in course_list:
            if course['id']==id:
                course['name']=request.form['name']
                course['fee']=request.form['fee']
                updated_course={
                    'id':id,
                    'name':course['name'],
                    'fee':course['fee']
                }
                return jsonify(updated_course)
            
            
    if request.method=='DELETE':
        for index,course in enumerate(course_list):
            if course['id']==id:
                course_list.pop(index)
                return jsonify(course_list)
  
if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)