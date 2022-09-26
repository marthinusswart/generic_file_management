from flask_restful import Api
from generic_file_management.api_management import ApiManagement
from generic_file_management.file_management import Files, FileManagement, FileDownload


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/api/v1')
    api.add_resource(Files, '/api/v1/<tenant_key>/files')
    api.add_resource(
        FileManagement, '/api/v1/<tenant_key>/files/<int:file_id>')
    api.add_resource(
        FileDownload, '/api/v1/<tenant_key>/downloads/<int:file_id>')
    return api
