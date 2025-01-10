from app import create_app
from app.utils.folder_utils import folder_init

app = create_app()

if __name__ == '__main__':
    folder_init()
    app.run(debug=True)
