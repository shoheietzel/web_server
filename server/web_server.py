"""
Flask web site with vocabulary matching game (identify vocabulary words that can be made from a scrambled string)
"""
import flask
import logging
import config                       # Our own module


############# Globals #############
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY  # Should allow using session variables


############# Pages #############
@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    return flask.render_template('homepage.html')


############# AJAX request handlers #############
# (return JSON, rather than rendering pages)
@app.route("/_check")
def check():
    """
    """
    app.logger.debug("Got a JSON request")
    rslt = {"test": True}
    return flask.jsonify(result=rslt)


############# Error handlers #############
@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


############# Main #############
if __name__ == "__main__":
    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(
            "Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
