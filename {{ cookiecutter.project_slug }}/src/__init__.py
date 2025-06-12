from dotenv import load_dotenv
from src.utils.logs import setup_logs
from src.utils.loading import start_loading
from src.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

def start_app():

    start_loading()
    load_dotenv()
    setup_logs()
    
    {{ cookiecutter.project_slug }}()

