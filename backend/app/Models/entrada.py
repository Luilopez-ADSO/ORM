from datetime import date

from . import db


class Entrada(db.Model):
    __tablename__ = "entradas"

    entra_id = db.Column(db.Integer, primary_key=True)
    entra_producto_id = db.Column(
        db.Integer,
        db.ForeignKey("productos.producto_id"),
        nullable=False,
    )
    entra_cantidad = db.Column(db.Integer, nullable=False)
    entra_factura = db.Column(db.String(100), nullable=False, default="")
    entra_stand = db.Column(db.String(50), nullable=False, default="")
    entra_ubicacion = db.Column(db.String(100), nullable=False, default="")
    entra_fecha = db.Column(db.Date, default=date.today)

    producto = db.relationship("Producto", back_populates="entradas")

    def to_dict(self):
        return {
            "id": self.entra_id,
            "producto_id": self.entra_producto_id,
            "cantidad": self.entra_cantidad,
            "factura": self.entra_factura,
            "stand": self.entra_stand,
            "ubicacion": self.entra_ubicacion,
            "fecha": self.entra_fecha.isoformat() if self.entra_fecha else None,
        }