from mangum import Mangum
from main import app  # Import FastAPI app dari root

handler = Mangum(app)
