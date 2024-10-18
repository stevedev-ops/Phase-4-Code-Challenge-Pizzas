class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'  # Fixed typo

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Restaurant {self.name}>'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
