from app import db

class Planet(db.Model):

    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    has_moons = db.Column(db.Boolean)

    def create_planet_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "has moons": self.has_moons
        }