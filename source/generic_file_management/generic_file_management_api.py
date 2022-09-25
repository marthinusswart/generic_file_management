from flask_restful import Api
from generic_file_management.api_management import ApiManagement
from generic_file_management.file_management import Files, FileManagement


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/')
    api.add_resource(Files, '/<tenant_key>/files')
    api.add_resource(FileManagement, '/<tenant_key>/files/<int:file_id>')
    return api
