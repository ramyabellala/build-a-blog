from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:code123@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'y337kGcys&zp38'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    blog = db.Column(db.String(500))

    def __init__(self, title,blog):
        self.title = title 
        self.blog = blog

@app.route('/newpost')
def index():
    return render_template('newpost.html')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    title_error =""
    blog_error = ""
    if request.method == 'POST' :
       input = request.form['title']
       entry = request.form['blog']

       if input =="" :
          title_error = "title is not given"
       if entry == "":
          blog_error = "blog is empty"
          title=""
    if not title_error and not blog_error :
       if input != "" :
            input_data = Blog(input , entry)
            db.session.add(input_data)
            db.session.commit()
            input_id = Blog.query.filter_by(title=input).first().id
#            return str(input_id)
            return redirect('/blog?id='+str(input_id))
    else:
        return render_template('/newpost.html',title_error=title_error,blog_error=blog_error)     

@app.route('/blog')
def post_blogs():
    blogs = Blog.query.all()
#    return str(blogs)
#    return str(request.args.get('id'))
    if request.args.get('id') == None :
        blogs = Blog.query.all()
#        return "blogs:" + str(blogs.title)
        return render_template('blog.html',blogs=blogs)
    elif request.args.get('id') != "" :
        input_id = request.args.get('id')
        input= Blog.query.filter_by(id=input_id).first().title
        entry= Blog.query.filter_by(id=input_id).first().blog
    #    return "in this loop:" + str(input_id) + "input:" + str(input) + "blog" + str(entry)
        return render_template('blog.html',input_id = input_id,input=input,entry=entry)
    
if __name__=='__main__':
    app.run()