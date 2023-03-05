from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.note import Note
from utils.db import db

notes = Blueprint("notes", __name__)

@notes.route('/')
def home():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@notes.route('/new', methods=['post'])
def add_note():
    code = int(request.form['code'])
    customer = request.form['customer']
    description = request.form['description']
    date = request.form['date']
    status = request.form['status']
    total = float(request.form['total'])

    new_note = Note(code, customer, description, date, status, total)
    
    db.session.add(new_note)
    db.session.commit()

    flash("La Remisión ha sido guardada de manera exitosa")

    return redirect(url_for('notes.home'))

@notes.route('/update/<id_note>', methods=['POST', 'GET'])
def update_note(id_note):
    note = Note.query.get(id_note)
    if request.method == 'POST':
        note.code = int(request.form["code"])
        note.customer = request.form['customer']
        note.description = request.form['description']
        note.date = request.form['date']
        note.status = request.form['status']
        note.total = float(request.form['total'])

        db.session.commit()

        flash("La Remisión ha sido actualizada de manera exitosa")

        return redirect(url_for("notes.home"))
        
    note = Note.query.get(id_note)
    return render_template('update.html', note=note)

@notes.route('/delete/<id_note>', methods=['GET'])
def delete_note(id_note):
    note = Note.query.get(id_note)
    db.session.delete(note)
    db.session.commit()

    flash("La Remisión ha sido eliminada de manera exitosa")
    
    return redirect(url_for('notes.home')) 

@notes.route('/search', methods=['POST'])
def test():
    type_filter = request.form['types_filter']
    
    if type_filter == 'code': 
            filtro = int(request.form['filter_input'])
            dataFilter = db.session.query(Note).filter(Note.code == filtro)
            
            
    elif type_filter == 'name':
        filtro = '%' + request.form["filter_input"][:3] + '%'
        print(filtro)
        dataFilter = db.session.query(Note).filter(Note.customer.like(filtro)).all()
        print(dataFilter)
        if len(dataFilter) == 0: 
            flash("No se encontraron registros con ese nombre")

         
    return render_template('index.html', notes=dataFilter)  