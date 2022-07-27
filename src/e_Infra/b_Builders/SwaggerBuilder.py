from custom_flask_swagger_ui import get_swaggerui_blueprint
from flask import redirect, request


# Method to build Swagger Blueprint #
def build_swagger_blueprint(lambda_handler):

    @lambda_handler.route('/swagger', methods=['GET'])
    def swagger_redirect():
        try:
            stage = request.aws_stage_name
        except:
            stage = None
        return redirect('/swagger/') if stage is None else redirect(f'/{stage}/swagger/')

    SWAGGER_URL = "/swagger"
    API_URL = "/swaggerdata"

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Swagger"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    lambda_handler.register_blueprint(swaggerui_blueprint)

