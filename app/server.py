from backend import create_app
import os

from dotenv import load_dotenv

# Load environment variables from .env file 
load_dotenv()

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', default=5000))

