from . import db


class Product(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'PRODUCT_INFO'
    productId = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    productName = db.Column(db.String(64), index=False, nullable=False, primary_key=True, autoincrement=False)
    productBrand = db.Column(db.String(64), index=False, nullable=False, primary_key=True, autoincrement=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    amount = db.Column(db.BigInteger, index=False, unique=False, nullable=False)
    quantity = db.Column(db.BigInteger, index=False, unique=False, nullable=False)

    def serialize(self):
        return {"productId": self.productId,
                "productName": self.productName,
                "productBrand": self.productBrand,
                "created": self.created,
                "amount": self.amount,
                "quantity": self.quantity}

    def __repr__(self):
        return '<Product {}>'.format(self.name)
