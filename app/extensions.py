# Setup the database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Setup the mail server
from flask_mail import Mail
mail = Mail()

# Setup the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()

# Setup the password crypting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# Setup the user login process
from flask_login import LoginManager
login_manager = LoginManager()

# Admin panel
from flask_admin import Admin
admin_panel = Admin(name='Admin', template_mode='bootstrap3')