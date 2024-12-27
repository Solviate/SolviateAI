
import sys
from src.api.routes import app
from src.utils.logger import log

def initialize_system():
    log("Initializing Solviate AI...")
    # Perform any setup steps here, such as loading configurations or connecting to services.

if __name__ == '__main__':
    initialize_system()
    try:
        log("Starting the Solviate AI server...")
        app.run(host='0.0.0.0', port=8000, debug=True)
    except KeyboardInterrupt:
        log("Solviate AI server shutting down gracefully.")
    except Exception as e:
        log(f"Unexpected error: {e}")
    