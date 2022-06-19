from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('firstName')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password is too short (<7).', category='error')
        else:
            # add user to database
            flash('Account created', category='success')



    return render_template("sign_up.html")