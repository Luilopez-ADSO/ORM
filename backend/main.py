from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

from app.Models import db, Producto, Categoria, Entrada
from app.Cammon import error_bp
from app.Cammon.config import Config
from app.Controller import productos_bp, categoria_bp, entrada_bp

# Crear aplicación 
app = Flask(__name__) 

# Configuración 
app.config.from_object(Config)

CORS(app)
swagger = Swagger(app) 
db.init_app(app) 

# Crear tablas automáticamente 
with app.app_context():     
    db.create_all()

# Ruta raíz 
@app.route("/", methods=["GET"]) 
def home():

    """
     Ruta de prueba para verificar que la API esté 
     funcionando
    """  
    return jsonify({"mensaje": "API está funcionando correctamente"}), 200
# Registrar blueprints 
app.register_blueprint(error_bp) 
app.register_blueprint(productos_bp) 
app.register_blueprint(categoria_bp) 
app.register_blueprint(entrada_bp)

if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=5000, debug=True)