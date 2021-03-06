"""
plugin.py

Base plugin for Grouper plugins. These are plugins that can be written to extend Grouper
functionality.
"""


class BasePlugin(object):
    def user_created(self, user):
        """Called when a new user is created

        When new users enter into Grouper, you might have reason to set metadata on those
        users for some reason. This method is called when that happens.

        Args:
            user (models.User): Object of new user.

        Returns:
            The return code of this method is ignored.
        """
        pass

    def configure(self, service_name):
        """
        Called once the plugin is instantiated to identify the executable
        (grouper-api or grouper-fe).
        """
        pass

    def log_exception(self, request, status, exception, stack):
        """
        Called when responding with statuses 400, 403, 404, and 500.

        Args:
            request (tornado.httputil.HTTPServerRequest): the request being handled.
            status (int): the response status.
            exception (Exception): either a tornado.web.HTTPError or an unexpected exception.
            stack (list): "pre-processed" stack trace entries for traceback.format_list.

        Returns:
            The return code of this method is ignored.
        """
        pass
