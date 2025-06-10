from flask import Flask,redirect,url_for,render_template,request
from models import db,Note

app=Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

from models import Note  


@app.route('/')
def home():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('home'))
 

if __name__ == '__main__': 
    with app.app_context():
        db.create_all()
    app.run(port=5000,debug=True)