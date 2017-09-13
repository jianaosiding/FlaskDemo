from init import app
from ui import index
from api import (
    douban,
    auth,
    collect,
    recommend,
    test,
)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
