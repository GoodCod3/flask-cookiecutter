from flask_restful import Resource, Api


class VersionView(Resource):
    def get(self):
        """
        This view returns the current version of the application.
        ---
        responses:
          200:
            description: Ok
            schema:
              type: string
        """
        return {
            "version": "pro-20230328v1"
        }