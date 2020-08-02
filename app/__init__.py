from flask import Flask,render_template,flash,redirect,url_for
from app.user.forms import RegistrationForm,LoginForm



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "hello"
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/register', methods=['GET','POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.email.data}','success')
            return redirect(url_for('home'))
        return render_template('register.html',form = form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            #flash(f'Account created for {form.email.data}', 'success')
            return redirect(url_for('home'))
        return render_template('login.html', form=form)


    return app