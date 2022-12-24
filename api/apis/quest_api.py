from core.services.quest_service import QuestService
from core.services.task_service import TaskService
from .models.utils import init_models, build_parser
from flask_restx import Namespace, Resource
from flask_cors import cross_origin
from flask_restx._http import HTTPStatus
import os
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import quest_models,\
    get_quest_response,\
    quest_model_with_tasks,\
    get_quests_response,\
    create_quest_request,\
    create_quest_response,\
    update_quest_request,\
    update_quest_response,\
    verify_quest_request,\
    verify_quest_response
import sys
sys.path.append("..")

api = Namespace('Quests', description='Quests related operation')
init_models(api, quest_models)

@cross_origin()
@api.route('/')
class Quest(Resource):

    @api.doc('quest')
    @api.response(200, model=get_quests_response, description="Success")
    @api.marshal_with(get_quests_response)
    def get(self):
        '''List quests'''
        quest_service = QuestService()

        quests = quest_service.get_all_quests()
        return {
            "success": True,
            "data": quests
        }

    

@api.route('/<int:id>')
class Quest(Resource):
    @api.doc('quest')
    @api.response(200, model=get_quest_response, description="Success")
    @api.marshal_with(get_quest_response)
    def get(self, id):
        '''Get a quest by id'''
        quest_service = QuestService()

        quest = quest_service.get_quest_by_id(id)

        if (quest):
            return {
                "success": True,
                "data": quest
            }
        else:
            api.abort(HTTPStatus.NOT_FOUND, {
                "success": False,
            })


@api.route('/<int:id>/verify')
class QuestVerify(Resource):
    @jwt_required(fresh=True)
    @api.doc('quest')
    @api.expect(verify_quest_request)
    @api.response(200, model=verify_quest_response, description="Success")
    @api.marshal_with(verify_quest_response)
    def post(self):
        '''Verify quest'''
        parser = build_parser(verify_quest_response)
        request = parser.parse_args()

        quest_service = QuestService()
        task_service = TaskService()

        quest_verify_status = quest_service.verify_quest()
        if quest_verify_status:
            return {
                "success": True,
                "data": verify_quest_response
            }

@api.route('/test')
class UserQuest(Resource):
    # @jwt_required(fresh=True)
    @ api.doc('users')
    @ api.response(200,description="Get quest's status  by user")

    def get(self):
        '''TEST'''

        a = os.system('node apis/hello.js')
        return a