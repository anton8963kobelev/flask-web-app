# Blueprint - позволяет разделять проект на набор независимых модулей
import json

from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import current_user, login_required

from . import db
from .models import Note

views = Blueprint('views', __name__)  # __name__ - имя исполняемого модуля


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Заметка не может быть пустой', category='error')
        else:
            new_note = Note(text=note, author=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Заметка добавлена', category='success')
    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    note_id = data['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.author == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
