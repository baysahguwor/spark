from unicodedata import name
from flask import flash, render_template, request, url_for, redirect
from application import application
from app.forms import RequestQouteForm, ContactUsForm
from app import mail
from flask_mail import Message
import os

@application.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', title='Page Error'), 404

@application.route('/')
@application.route('/index', methods=['GET', 'POST'])
def index():
    form = RequestQouteForm()

    # recieve data from form and send email to sparksolution70@gmail.com
    if form.validate_on_submit():
        phone = form.phone.data
        name = form.name.data 
        email = form.email.data
        description = form.description.data

        reciever = 'sparksolution70@gmail.com'
        # sending Message 
        msg = Message('Costumer Inquiry', sender='melvinkonneh3@gmail.com', recipients=[reciever])
        msg.body = f"Costumer name '{name}',  'Costumer number '{phone}', Costumer Email '{email}',  Costumer Description '{description}' "
        mail.send(msg)



        flash('Thank You, We recieve your message And will Contact you Shortly')
        return redirect(request.referrer)


    return render_template('index.html', title='Spark Solutions', form=form)

@application.route('/contact_us', methods = ['GET', 'POST'])
def contact_us():
    form = ContactUsForm()

    # recieve data from form and send email to sparksolution70@gmail.com
    if form.validate_on_submit():
        phone = form.phone.data
        name = form.name.data 
        email = form.email.data
        description = form.description.data

        reciever = 'sparksolution70@gmail.com'
        # sending Message 
        msg = Message('Costumer Inquiry', sender='melvinkonneh3@gmail.com', recipients=[reciever])
        msg.body = f"Costumer name '{name}',  'Costumer number '{phone}', Costumer Email '{email}',  Costumer Description '{description}' "
        mail.send(msg)
        flash('Thank You, We recieve your message And will Contact you Shortly')
        return redirect( url_for('index'))
    return render_template('contact_us.html', title='Contact Us', form=form)

@application.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Spark Solutions')


@application.route('/it_solutions')
def it_solutions():
    return render_template('it_solutions.html', title='IT Solutions')

@application.route('/web-app-development')
def web_app_development():
    return render_template('web-app-development.html', title='Web App Development')

@application.route('/mobile-app-development')
def mobile_app_development():
    return render_template('mobile-app-development.html', title='Mobile App Development')

@application.route('/data-entry')
def data_entry():
    return render_template('data-entry.html', title='Data Entry')

@application.route('/data-analysis')
def data_analysis():
    return render_template('data-analysis.html', title='Data Analysis')




