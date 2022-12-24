from .models.utils import init_models, build_parser
from core.services.community_service import CommunityService
from core.services.quest_service import QuestService
from .exceptions import DataValidationException
from core.services.exceptions import ResourceNotFoundException
from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
import re
from .models import community_models,\
    get_community_response,\
    create_community_request,\
    create_community_response,\
    update_community_request,\
    update_community_response,\
    create_quest_model,\
    create_quest_response,\
    update_quest_request,\
    update_quest_response
    
    


api = Namespace('Community', description='Communities related operation')


init_models(api, community_models)


@api.route('/<string:slug>')
class Community(Resource):
    @api.doc('community')
    @api.response(200, model=get_community_response, description="Success")
    @api.marshal_with(get_community_response)
    def get(self, slug):
        '''List a community'''
        community_service = CommunityService()
        community = community_service.get_community_by_slug(slug=slug)
        if community:
            return {
                "success": True,
                "data": community
            }
        else:
            raise ResourceNotFoundException('Community not found')

    @jwt_required(fresh=True)
    @api.doc('community')
    @api.expect(update_community_request)
    @api.response(200, model=update_community_response, description="Success")
    @api.marshal_with(update_community_response)
    def put(self, slug):
        '''Update community'''
        parser = build_parser(update_community_request)
        request = parser.parse_args()

        community_service = CommunityService()

        update_community = community_service.update_community(
            slug=slug, data=request)

        return {
            "success": True,
            "data": update_community
        }


@api.route('/')
class Community(Resource):
    @jwt_required(fresh=True)
    @api.doc('community')
    @api.expect(create_community_request)
    @api.response(200, model=create_community_response, description="Success")
    @api.marshal_with(create_community_response)
    def post(self):
        '''Create community'''
        parser = build_parser(create_community_request)
        request = parser.parse_args()
        print(request)
        if re.match("^[A-Za-z0-9]*$", request['urlSlug']):
            community_service = CommunityService()

            create_community = community_service.create_community(
                user_id=get_jwt_identity(), data=request)
        else:
            raise DataValidationException('Slug is not validated')

        

        return {
            "success": True,
            "data": create_community
        }

    @api.doc('community')
    @api.response(200, model=get_community_response, description="Success")
    @api.marshal_with(get_community_response)
    def get(self):
        '''List all communites'''
        community_service = CommunityService()
        all_communities = community_service.get_all_communities()
        return {
            "success": True,
            "data": all_communities
        }

@api.route('/<string:slug>/quests/<int:id>')
class Community(Resource):
    # @jwt_required(fresh=True)
    @api.doc('quest')
    @api.expect(update_quest_request)
    @api.response(200, model=update_quest_response, description="Success")
    @api.marshal_with(code=HTTPStatus.OK, fields=update_quest_response)
    # @api.marshal_with(code = HTTPStatus.BAD_REQUEST ,field=update_quest_response)
    def put(self,id,slug):
        '''Update quest'''
        parser = build_parser(update_quest_request)
        request = parser.parse_args()

        quest_service = QuestService()

        update_quest = quest_service.update_quest(id=id,slug=slug, update_data=request)

        return {
            "success": True,
            "data": update_quest
        }

   

@api.route('/<string:slug>/quests/')
class Community(Resource):
    # @jwt_required(fresh=True)
    @api.doc('quest')
    @api.expect(create_quest_model,  validate=True)
    @api.response(200, model=create_quest_response, description="Success")
    @api.marshal_with(create_quest_response)
    def post(self,slug):
        '''Create quest'''
        # identity = get_jwt_identity()

        parser = build_parser(create_quest_model)
        request = parser.parse_args()

        quest_service = QuestService()

        create_quest = quest_service.create_quest(
            slug=slug, data=request)

        return {
            "success": True,
            "data": create_quest
        }