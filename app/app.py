from flask import Flask, render_template
from app import commands, admin
from app.views import user, predict, main
from app.models import User
from app.extensions import bcrypt, db, toolbar, login_manager, mail, admin_panel
import os.path as op

def create_app(config_object='app.settings'):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_admins(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'userbp.signin'
    toolbar.init_app(app)
    mail.init_app(app)
    admin_panel.init_app(app)
    #from app.logger_setup import logger
    return None

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(user.userbp)
    app.register_blueprint(main.mainbp)
    app.register_blueprint(predict.predictbp)
    return None

def register_admins(app):
    """Register Flask admins."""
    # Users
    admin_panel.add_view(admin.ModelView(User, db.session))

    # Static files
    path = op.join(op.dirname(__file__), 'static')
    admin_panel.add_view(admin.FileAdmin(path, '/static/', name='Static'))
    return None

def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('error.html', message=error_code, title=error_code), error_code
    for errcode in [401, 404, 410, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_shellcontext(app):
    def shell_context():
            """Shell context objects."""
            return {
                'app': app
                }

    app.shell_context_processor(shell_context)

def register_commands(app):
    app.cli.add_command(commands.initdb)
    app.cli.add_command(commands.dropdb)
    app.cli.add_command(commands.recycledb)