from . import db

class Property(db.Model):

    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.String)
    bathrooms = db.Column(db.String)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, bedrooms, bathrooms, price, location, property_type, photo):
        self.title = title
        self.description = description
        self.price = price
        self.property_type = property_type
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.location = location
        self.photo = photo      
