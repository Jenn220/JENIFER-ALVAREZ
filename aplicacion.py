from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Universo de Jenifer - Física Cósmica</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1e0533 0%, #2d1b4e 25%, #1a0b2e 50%, #0f051d 100%);
            color: #ffffff;
            overflow-x: hidden;
            min-height: 100vh;
            position: relative;
        }
        
        /* Estrellas de fondo */
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }
        
        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
        
        /* Planetas orbitando */
        .orbit-container {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 1;
            pointer-events: none;
        }
        
        .orbit {
            position: absolute;
            border: 1px solid rgba(138, 43, 226, 0.2);
            border-radius: 50%;
            animation: rotate 20s linear infinite;
        }
        
        .orbit1 { width: 300px; height: 300px; margin: -150px; }
        .orbit2 { width: 500px; height: 500px; margin: -250px; animation-duration: 30s; }
        .orbit3 { width: 700px; height: 700px; margin: -350px; animation-duration: 40s; }
        
        .planet {
            position: absolute;
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
        }
        
        .planet1 {
            width: 15px;
            height: 15px;
            background: linear-gradient(135deg, #ff6b9d, #c06c84);
            top: 0;
            left: 50%;
            margin-left: -7.5px;
        }
        
        .planet2 {
            width: 20px;
            height: 20px;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            top: 0;
            left: 50%;
            margin-left: -10px;
        }
        
        .planet3 {
            width: 25px;
            height: 25px;
            background: linear-gradient(135deg, #f093fb, #f5576c);
            top: 0;
            left: 50%;
            margin-left: -12.5px;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        /* Contenedor principal */
        .container {
            position: relative;
            z-index: 2;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        /* Header */
        .header {
            text-align: center;
            margin-bottom: 50px;
            animation: fadeInDown 1s ease-out;
        }
        
        .header h1 {
            font-size: 3em;
            background: linear-gradient(45deg, #ff6ec4, #7873f5, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
            text-shadow: 0 0 30px rgba(138, 43, 226, 0.5);
        }
        
        .header p {
            font-size: 1.2em;
            color: #b19cd9;
            font-style: italic;
        }
        
        /* Tarjetas de operaciones */
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-bottom: 50px;
        }
        
        .card {
            background: rgba(138, 43, 226, 0.1);
            border: 2px solid rgba(138, 43, 226, 0.3);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            animation: fadeInUp 1s ease-out;
        }
        
        .card:hover {
            transform: translateY(-10px);
            border-color: rgba(138, 43, 226, 0.8);
            box-shadow: 0 10px 40px rgba(138, 43, 226, 0.4);
        }
        
        .card h2 {
            color: #ff6ec4;
            margin-bottom: 15px;
            font-size: 1.8em;
        }
        
        .card a {
            display: inline-block;
            margin-top: 15px;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        
        .card a:hover {
            transform: scale(1.1);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.6);
        }
        
        /* Sección de física */
        .physics-section {
            background: rgba(30, 5, 51, 0.5);
            border: 2px solid rgba(138, 43, 226, 0.3);
            border-radius: 20px;
            padding: 40px;
            margin-top: 50px;
            backdrop-filter: blur(10px);
            animation: fadeIn 1.5s ease-out;
        }
        
        .physics-section h2 {
            text-align: center;
            color: #7873f5;
            margin-bottom: 30px;
            font-size: 2em;
        }
        
        .physics-facts {
            display: grid;
            gap: 20px;
        }
        
        .fact {
            background: rgba(138, 43, 226, 0.1);
            padding: 20px;
            border-left: 4px solid #ff6ec4;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .fact:hover {
            background: rgba(138, 43, 226, 0.2);
            transform: translateX(10px);
        }
        
        .fact h3 {
            color: #4facfe;
            margin-bottom: 10px;
        }
        
        .fact p {
            color: #b19cd9;
            line-height: 1.6;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 30px;
            color: #7873f5;
            font-style: italic;
        }
        
        /* Animaciones */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            .cards-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Estrellas de fondo -->
    <div class="stars" id="stars"></div>
    
    <!-- Planetas orbitando -->
    <div class="orbit-container">
        <div class="orbit orbit1">
            <div class="planet planet1"></div>
        </div>
        <div class="orbit orbit2">
            <div class="planet planet2"></div>
        </div>
        <div class="orbit orbit3">
            <div class="planet planet3"></div>
        </div>
    </div>
    
    <!-- Contenido principal -->
    <div class="container">
        <div class="header">
            <h1>🌌 Universo de Jenifer 🌌</h1>
            <p>Explorando la física del cosmos - 14 de Noviembre 2025</p>
        </div>
        
        <div class="cards-container">
            <div class="card">
                <h2>➕ Suma Cósmica</h2>
                <p>Calcula la fusión de estrellas</p>
                <a href="/suma/5/3">5 + 3 = ?</a>
            </div>
            
            <div class="card">
                <h2>➖ Resta Estelar</h2>
                <p>Mide la expansión del universo</p>
                <a href="/resta/10/4">10 - 4 = ?</a>
            </div>
        </div>
        
        <div class="physics-section">
            <h2>⭐ Datos Fascinantes del Universo ⭐</h2>
            <div class="physics-facts">
                <div class="fact">
                    <h3>🌠 Velocidad de la Luz</h3>
                    <p>La luz viaja a 299,792,458 metros por segundo. A esta velocidad, podrías dar la vuelta a la Tierra 7.5 veces en un solo segundo.</p>
                </div>
                
                <div class="fact">
                    <h3>🪐 Agujeros Negros</h3>
                    <p>Un agujero negro puede tener una masa millones de veces mayor que nuestro Sol, pero comprimida en un espacio increíblemente pequeño.</p>
                </div>
                
                <div class="fact">
                    <h3>🌌 Galaxias</h3>
                    <p>Se estima que existen más de 2 billones de galaxias en el universo observable, cada una con miles de millones de estrellas.</p>
                </div>
                
                <div class="fact">
                    <h3>⚛️ Materia Oscura</h3>
                    <p>El 85% de la materia del universo es "oscura" - no podemos verla directamente, pero sabemos que existe por sus efectos gravitacionales.</p>
                </div>
                
                <div class="fact">
                    <h3>🌟 Estrellas</h3>
                    <p>Hay más estrellas en el universo que granos de arena en todas las playas de la Tierra. ¡Aproximadamente 10^24!</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>✨ Creado por Jenifer Alvarez - Explorando el infinito ✨</p>
            <p>Desplegado con Docker + Traefik + GitHub Actions</p>
        </div>
    </div>
    
    <script>
        // Generar estrellas aleatorias
        const starsContainer = document.getElementById('stars');
        const numStars = 200;
        
        for (let i = 0; i < numStars; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 3 + 's';
            starsContainer.appendChild(star);
        }
    </script>
</body>
</html>
    '''

@app.route('/suma/<path:a>/<path:b>')
def sumar(a, b):
    try:
        a = int(a)
        b = int(b)
        resultado = a + b
        return f'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suma Cósmica</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e0533 0%, #2d1b4e 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }}
        .result-container {{
            text-align: center;
            background: rgba(138, 43, 226, 0.2);
            padding: 50px;
            border-radius: 20px;
            border: 2px solid rgba(138, 43, 226, 0.5);
            backdrop-filter: blur(10px);
        }}
        h1 {{
            font-size: 3em;
            color: #ff6ec4;
            margin-bottom: 20px;
        }}
        .calculation {{
            font-size: 2em;
            color: #4facfe;
            margin: 20px 0;
        }}
        .result {{
            font-size: 4em;
            background: linear-gradient(45deg, #ff6ec4, #7873f5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }}
        a {{
            display: inline-block;
            margin-top: 30px;
            padding: 15px 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-size: 1.2em;
            transition: all 0.3s;
        }}
        a:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.6);
        }}
    </style>
</head>
<body>
    <div class="result-container">
        <h1>✨ Suma Cósmica ✨</h1>
        <div class="calculation">{a} + {b} =</div>
        <div class="result">{resultado}</div>
        <a href="/">← Volver al Universo</a>
    </div>
</body>
</html>
        '''
    except:
        return '<h1>Error: Ingresa números válidos</h1>'

@app.route('/resta/<path:a>/<path:b>')
def restar(a, b):
    try:
        a = int(a)
        b = int(b)
        resultado = a - b
        return f'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resta Estelar</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f051d 0%, #1a0b2e 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }}
        .result-container {{
            text-align: center;
            background: rgba(138, 43, 226, 0.2);
            padding: 50px;
            border-radius: 20px;
            border: 2px solid rgba(138, 43, 226, 0.5);
            backdrop-filter: blur(10px);
        }}
        h1 {{
            font-size: 3em;
            color: #7873f5;
            margin-bottom: 20px;
        }}
        .calculation {{
            font-size: 2em;
            color: #4facfe;
            margin: 20px 0;
        }}
        .result {{
            font-size: 4em;
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }}
        a {{
            display: inline-block;
            margin-top: 30px;
            padding: 15px 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-size: 1.2em;
            transition: all 0.3s;
        }}
        a:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.6);
        }}
    </style>
</head>
<body>
    <div class="result-container">
        <h1>🌟 Resta Estelar 🌟</h1>
        <div class="calculation">{a} - {b} =</div>
        <div class="result">{resultado}</div>
        <a href="/">← Volver al Universo</a>
    </div>
</body>
</html>
        '''
    except:
        return '<h1>Error: Ingresa números válidos</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)