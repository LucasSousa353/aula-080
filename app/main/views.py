from flask import render_template, session, redirect, url_for, flash
from app import app, db
from app.main.forms import NameForm
from app.models import User
from app.main.email import send_simple_message

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            # Enviar e-mail usando a função Mailgun e obter resultado
            email_result = send_simple_message(
                subject="Novo Usuário Registrado",
                text=f"Um novo usuário foi registrado: {form.name.data}"
            )
            flash(email_result, 'info')

        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))

    pessoas = User.query.all()
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), pessoas=pessoas)
