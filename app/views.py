"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash

from .models import Property
from .forms import PropertyForm

from werkzeug.utils import secure_filename
from flask import send_from_directory

from . import db

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
    return render_template('about.html', name="Martin Bartley")


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


# Define the routes and their corresponding view functions
@app.route('/properties/create', methods=['GET', 'POST'])
def form():
    form = PropertyForm()
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        description = request.form['description']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        location = request.form['location']
        price = request.form['price']
        prop_type = request.form['type']

        # Get file and save to upload folder
        photo_file = request.files['photo']
        filename = secure_filename(photo_file.filename)
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Create new property object and add to database
        new_prop = Property(title=title, description=description, bedrooms=bedrooms, bathrooms=bathrooms, location=location, price=price, type=prop_type, photo=filename)
        db.session.add(new_prop)
        db.session.commit()

        flash('Property added successfully', 'success')
        return redirect(url_for('properties'))

    return render_template('form.html',form=form)

@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def property(propertyid):
    property = Property.query.get(propertyid)
    return render_template('property.html', property=property)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
