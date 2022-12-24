from core.services.task_service import TaskService
from .models import operation_response_model
from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
import sys
sys.path.append("..")

api = Namespace('Tasks', description='Tasks related operation')


@api.route('/<int:id>/verify')
class TaskVerify(Resource):
    @jwt_required(fresh=True)
    @api.doc('task')
    @api.response(HTTPStatus.OK, model=operation_response_model, description="Success")
    def post(self, id):
        '''Verify  task'''

        task_service = TaskService()
        is_verified = task_service.verify_task(id, get_jwt_identity())

        return {
            "success": is_verified
        }, HTTPStatus.OK
