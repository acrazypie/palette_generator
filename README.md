# Palette Generator 🎨

[English](#english) | [Italiano](#italiano)

---

## Italiano

### Descrizione

**Palette Generator** è un'applicazione web moderna e intuitiva per generare palette di colori in modo dinamico. Permette di creare palette di colori utilizzando diverse algoritmi di generazione, basati su un colore base selezionato dall'utente.

### Caratteristiche Principali

✨ **6 Modi di Generazione Palette**

-   **Analogous**: Colori adiacenti sulla ruota cromatica
-   **Complementary**: Colore base + colore opposto
-   **Triadic**: 3 colori equidistanti (120° apart)
-   **Tetradic**: 4 colori formando un rettangolo
-   **Monochromatic**: Variazioni di saturazione e luminosità
-   **Shades and Tints**: Versioni più scure e più chiare

🎯 **Funzionalità Avanzate**

-   Selezione colore interattiva con color picker
-   Generazione palette in tempo reale
-   Copia colori negli appunti con un click
-   Notifiche di feedback
-   Adattamento automatico del contrasto del testo
-   Personalizzazione numero di colori (3-12)

📱 **Design Responsivo**

-   Interfaccia pulita e moderna
-   Compatibile con desktop e dispositivi mobili
-   UX intuitiva

🐳 **Pronto per Docker**

-   Immagini Docker per produzione e sviluppo
-   Docker Compose configurato
-   Facilmente deployabile

🌓 **Dark/Light Theme**

-   Toggle tra tema scuro e chiaro
-   Preferenza salvata in localStorage
-   Transizioni smooth tra i temi
-   Supporto completo per entrambi i temi

📱 **Fully Responsive**

-   Design mobile-first con media query
-   Breakpoint per tablet (768px) e mobile (480px)
-   Color-box visualizzati in colonna su dispositivi mobili
-   Controls ottimizzati per touch
-   Interfaccia fluida su tutte le risoluzioni

### Installazione Locale

#### Prerequisiti

-   Python 3.8+
-   pip
-   Virtual environment (consigliato)

#### Setup

1. **Clona il repository**

```bash
git clone <repository-url>
cd palette_generator
```

2. **Crea virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

3. **Installa dipendenze**

```bash
pip install -r requirements.txt
```

4. **Configura variabili d'ambiente**

```bash
cp .env.example .env
```

5. **Avvia l'applicazione**

```bash
python run.py
```

L'applicazione sarà disponibile su: **http://localhost:5000**

### Utilizzo con Docker

#### Avvio Rapido (Produzione)

```bash
docker-compose up -d
```

L'applicazione sarà disponibile su: **http://localhost:5000**

#### Avvio Sviluppo

```bash
docker-compose -f docker-compose.dev.yml up
```

Con hot reload e debug mode abilitato.

#### Comandi Utili

```bash
# Visualizza log
docker logs -f palette_generator

# Esegui shell nel container
docker exec -it palette_generator bash

# Ferma l'applicazione
docker-compose down

# Ricostruisci immagine
docker-compose build --no-cache
```

### Struttura del Progetto

```
palette_generator/
├── app/
│   ├── __init__.py           # Inizializzazione Flask
│   ├── palette.py            # Algoritmi generazione palette
│   ├── routes.py             # Route API
│   ├── templates/
│   │   ├── base.html         # Template base
│   │   └── index.html        # Template principale
│   └── static/
│       ├── css/
│       │   └── style.css     # Stili CSS
│       └── js/
│           └── main.js       # JavaScript frontend
├── config.py                 # Configurazione applicazione
├── run.py                    # Entry point
├── requirements.txt          # Dipendenze Python
├── Dockerfile                # Immagine produzione
├── Dockerfile.dev            # Immagine sviluppo
├── docker-compose.yml        # Orchestrazione produzione
├── docker-compose.dev.yml    # Orchestrazione sviluppo
├── .env.example              # Variabili d'ambiente esempio
├── .env                      # Variabili d'ambiente (locale)
├── .gitignore                # File esclusi da git
├── .dockerignore             # File esclusi da Docker
└── README.md                 # Questo file
```

### API Endpoints

#### POST /api/generate

Genera una palette di colori basata sui parametri forniti.

**Request Body:**

```json
{
    "base_color": "#3498db",
    "mode": "analogous",
    "count": 5
}
```

**Parametri:**

-   `base_color` (string): Colore base in formato hex (default: "#3498db")
-   `mode` (string): Modalità di generazione (default: "analogous")
    -   Valori: `analogous`, `complementary`, `triadic`, `tetradic`, `monochromatic`, `shades_and_tints`
-   `count` (integer): Numero di colori da generare (default: 5)

**Response Success:**

```json
{
    "palette": ["#3498db", "#5dade2", "#85c1e9", "#aed6f1", "#d6eaf8"],
    "success": true
}
```

**Response Error:**

```json
{
    "error": "Invalid hex color: invalid",
    "success": false
}
```

### Configurazione

#### Variabili d'Ambiente

Crea o modifica il file `.env`:

```env
# Flask Configuration
FLASK_ENV=development           # development | production
FLASK_APP=run.py
FLASK_DEBUG=0                   # 0 | 1

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Application Settings
SECRET_KEY=your-secret-key-here
```

### Sviluppo

#### Requisiti per lo Sviluppo

```bash
pip install -r requirements.txt
pip install pytest pytest-cov  # Per testing
```

#### Esecuzione in Modalità Debug

```bash
FLASK_DEBUG=1 python run.py
```

#### Testing

```bash
pytest              # Esegui tutti i test
pytest -v           # Verbose
pytest --cov        # Con coverage
```

### Deployment

#### Produzione con Gunicorn

```bash
pip install gunicorn
gunicorn --workers 4 --worker-class sync run:app
```

#### Con Docker

```bash
# Build immagine
docker build -t palette-generator:latest .

# Esegui container
docker run -p 5000:5000 palette-generator:latest
```

#### Pubblicazione su Registry

```bash
# Tag immagine
docker tag palette-generator:latest myregistry.com/palette-generator:latest

# Push
docker push myregistry.com/palette-generator:latest
```

### Contribuire

Le pull request sono benvenute! Per modifiche importanti, aprire prima un issue per discutere le modifiche proposte.

### Licenza

Questo progetto è disponibile sotto la licenza MIT. Vedi il file LICENSE per dettagli.

### Support

Per problemi, domande o suggerimenti, apri un issue su GitHub o contatta il team di sviluppo.

---

## English

### Description

**Palette Generator** is a modern and intuitive web application for generating color palettes dynamically. It allows you to create color palettes using various generation algorithms, based on a base color selected by the user.

### Key Features

✨ **6 Palette Generation Modes**

-   **Analogous**: Adjacent colors on the color wheel
-   **Complementary**: Base color + opposite color
-   **Triadic**: 3 equally spaced colors (120° apart)
-   **Tetradic**: 4 colors forming a rectangle
-   **Monochromatic**: Variations of saturation and brightness
-   **Shades and Tints**: Darker and lighter versions

🎯 **Advanced Features**

-   Interactive color selection with color picker
-   Real-time palette generation
-   Copy colors to clipboard with one click
-   Feedback notifications
-   Automatic text contrast adjustment
-   Customizable number of colors (3-12)

📱 **Responsive Design**

-   Clean and modern interface
-   Compatible with desktop and mobile devices
-   Intuitive UX

🐳 **Docker Ready**

-   Docker images for production and development
-   Docker Compose configured
-   Easily deployable

### Local Installation

#### Prerequisites

-   Python 3.8+
-   pip
-   Virtual environment (recommended)

#### Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd palette_generator
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
cp .env.example .env
```

5. **Start the application**

```bash
python run.py
```

The application will be available at: **http://localhost:5000**

### Docker Usage

#### Quick Start (Production)

```bash
docker-compose up -d
```

The application will be available at: **http://localhost:5000**

#### Development Startup

```bash
docker-compose -f docker-compose.dev.yml up
```

With hot reload and debug mode enabled.

#### Useful Commands

```bash
# View logs
docker logs -f palette_generator

# Execute shell in container
docker exec -it palette_generator bash

# Stop the application
docker-compose down

# Rebuild image
docker-compose build --no-cache
```

### Project Structure

```
palette_generator/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── palette.py               # Palette generation algorithms (6 modes)
│   ├── routes.py                # API routes & endpoints
│   ├── templates/
│   │   ├── base.html            # Base HTML template
│   │   └── index.html           # Main template with controls
│   └── static/
│       ├── css/
│       │   └── style.css        # Responsive styles (dark/light theme)
│       ├── js/
│       │   ├── main.js          # Palette generator & theme manager
│       │   └── theme.js         # Deprecated (managed by main.js)
│       └── fonts/
│           └── Outfit-Regular.ttf
├── config.py                    # Application configuration
├── run.py                       # Flask entry point
├── wsgi.py                      # WSGI/Gunicorn configuration
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (local)
├── .env.example                 # Example environment variables
├── .gitignore                   # Git ignore rules
├── .dockerignore                # Docker ignore rules
│
├── Docker Configuration
├── Dockerfile                   # Production image
├── Dockerfile.dev               # Development image
├── docker-compose.yml           # Production orchestration
├── docker-compose.dev.yml       # Development orchestration
├── docker-entrypoint.sh         # Docker entrypoint script
│
├── Utility Scripts
├── build-docker.sh              # Build & push Docker image script
├── docker-manage.sh             # Docker management CLI
│
├── Documentation
├── README.md                    # Main documentation (IT/EN)
├── README_DOCKER.md             # Docker setup guide
└── DOCKER_DEPLOYMENT.md         # Docker deployment guide
```

### API Endpoints

#### POST /api/generate

Generates a color palette based on provided parameters.

**Request Body:**

```json
{
    "base_color": "#3498db",
    "mode": "analogous",
    "count": 5
}
```

**Parameters:**

-   `base_color` (string): Base color in hex format (default: "#3498db")
-   `mode` (string): Generation mode (default: "analogous")
    -   Values: `analogous`, `complementary`, `triadic`, `tetradic`, `monochromatic`, `shades_and_tints`
-   `count` (integer): Number of colors to generate (default: 5)

**Success Response:**

```json
{
    "palette": ["#3498db", "#5dade2", "#85c1e9", "#aed6f1", "#d6eaf8"],
    "success": true
}
```

**Error Response:**

```json
{
    "error": "Invalid hex color: invalid",
    "success": false
}
```

### Configuration

#### Environment Variables

Create or edit the `.env` file:

```env
# Flask Configuration
FLASK_ENV=development           # development | production
FLASK_APP=run.py
FLASK_DEBUG=0                   # 0 | 1

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Application Settings
SECRET_KEY=your-secret-key-here
```

### Development

#### Development Requirements

```bash
pip install -r requirements.txt
pip install pytest pytest-cov  # For testing
```

#### Running in Debug Mode

```bash
FLASK_DEBUG=1 python run.py
```

#### Testing

```bash
pytest              # Run all tests
pytest -v           # Verbose
pytest --cov        # With coverage
```

### Deployment

#### Production with Gunicorn

```bash
pip install gunicorn
gunicorn --workers 4 --worker-class sync run:app
```

#### With Docker

```bash
# Build image
docker build -t palette-generator:latest .

# Run container
docker run -p 5000:5000 palette-generator:latest
```

#### Publishing to Registry

```bash
# Tag image
docker tag palette-generator:latest myregistry.com/palette-generator:latest

# Push
docker push myregistry.com/palette-generator:latest
```

### Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the proposed changes.

### License

This project is available under the MIT License. See the LICENSE file for details.

### Tech Stack

**Backend:**

-   Python 3.11
-   Flask 3.1.2
-   Colorsys (Python standard library)

**Frontend:**

-   HTML5 with Jinja2 templating
-   CSS3 (Flexbox, Media Queries, CSS Variables)
-   Vanilla JavaScript (ES6+)
-   LocalStorage API

**DevOps:**

-   Docker & Docker Compose
-   Python Virtual Environment
-   Gunicorn WSGI server

**Features:**

-   6 color generation algorithms
-   Dark/Light theme toggle
-   Fully responsive design (Mobile, Tablet, Desktop)
-   Real-time palette generation
-   Copy to clipboard functionality
-   Local theme preference persistence

### Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

---

**Made with ❤️ by Elisa**
**Consider supporting the project with a star on GitHub!**
