from flask import render_template, url_for, redirect, request
#from flask import (render_template, url_for, request)

from models import db, Project, app

@app.route('/')
def index():   
    projects = Project.query.all()
    return render_template('index.html')

@app.route('/projects/new', methods = ['GET', 'POST'])
def new():
    if request.form:        
        new_project = Project(title=request.form['title'], 
                                description=request.form['desc'],
                                skills=request.form['skills'], 
                                url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

@app.route('/projects/<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)

@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        return redirect (url_for('index'))
    return render_template('editproject.html', project=project)

@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')