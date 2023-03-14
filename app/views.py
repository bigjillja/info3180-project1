"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, flash, request, redirect, url_for
from .forms import MyForm, PhotoForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create')
def create():
    formdata = MyForm()
    if formdata.validate_on_submit():
            title = formdata.title.data
            description = formdata.description.data
            price = formdata.price.data
            rooms = formdata.rooms.data
            bathrooms = formdata.bathrooms.data
            property_type = formdata.property_type.data
            location = formdata.location.data

            flash('Your response has been recorded!', 'success')

    flash_errors(formdata)
    return render_template('addproperty.html', title=title,
                                   description=description,
                                   rooms=rooms,
                                   bathrooms=bathrooms,
                                   price=price,
                                   property_type=property_type,
                                   location=location)

@app.route('/properties')
def viewproperties():
    return render_template('viewproperties.html')

@app.route('/properties/<propertyid>')
def viewpropertyid():
    return render_template('viewpropertyid.html')

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Invalid data! Check %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
