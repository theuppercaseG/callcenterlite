from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, CallLog
from . import db, login_manager
from twilio.rest import Client
from config import Config

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        to_number = request.form['to_number']
        client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=to_number,
            from_=Config.TWILIO_PHONE_NUMBER
        )
        new_log = CallLog(to_number=to_number, status='initiated')
        db.session.add(new_log)
        db.session.commit()
        flash('Call initiated to ' + to_number)
    logs = CallLog.query.order_by(CallLog.timestamp.desc()).all()
    return render_template('dashboard.html', logs=logs)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# 🔟 راوتات purpsystem1 إلى purpsystem10
def generate_purpsystem_routes():
    for i in range(1, 11):
        route_name = f"/purpsystem{i}"
        template_name = f"purpsystem{i}.html"
        endpoint_name = f"purpsystem{i}"

        def view(template=template_name):
            return render_t_
