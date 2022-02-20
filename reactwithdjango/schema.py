import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
import graphql_jwt



from rctdj.models import Movie

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "name", "description")


class Query(UserQuery, MeQuery, graphene.ObjectType):
	all_movie = graphene.List(MovieType)
	movie_by_name = graphene.Field(MovieType, name=graphene.String(required=True))
	# movie_by_name = graphene.Field(MovieType, movie_id=graphene.Int())
	def resolve_all_movie(root, info):
		return Movie.objects.all()

	def resolve_movie_by_name(root, info, name):
		try:
			return Movie.objects.get(name=name)
		except Movie.DoesNotExist:
			return None
	# def resolve_movie_by_name(self, info, movie_id):
 #        return Movie.objects.get(pk=book_id)

# class MovieInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     description = graphene.String()

# class CreateMovie(graphene.Mutation):
#     class Arguments:
#         movie_data = MovieInput(required=True)

#     movie = graphene.Field(MovieType)

#     @staticmethod
#     def mutate(root, info, movie_data=None):
#         movie_instance = Movie( 
#             name=movie_data.name,
#             description=movie_data.description,
          
#         )
#         movie_instance.save()
#         return CreateMovie(movie=movie_instance)

class CreateMovie(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    #3
    def mutate(self, info, name, description):
        movie = Movie(name=name, description=description)
        movie.save()

        return CreateMovie(
            id=movie.id,
            name=movie.name,
            description=movie.description,
        )
# guery of above mutation
# mutation{
#   createMovie(name:"sam", description:"hello"){
#     id,
#     name,
#     description
#   }
# }

# class UpdateMovie(graphene.Mutation):
#     class Arguments:
#         movie_data = MovieInput(required=True)

#     movie = graphene.Field(MovieType)

#     @staticmethod
#     def mutate(root, info, movie_data=None):

#         movie_instance = Movie.objects.get(pk=movie_data.id)

#         if movie_instance:
#             movie_instance.name = movie_data.name
#             movie_instance.description = movie_data.description
#             movie_instance.save()

#             return UpdateMovie(movie=movie_instance)
#         return UpdateMovie(movie=None)
class UpdateMovie(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()

    #2
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()

    movie = graphene.Field(MovieType)
    
    @staticmethod
    def mutate(root, info, id, name, description):

        movie = Movie.objects.get(pk=id)
        movie.name = name
        movie.description = description
        movie.save()
        
        return UpdateMovie(movie=movie)

class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    Movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id):
        movie_instance = Movie.objects.get(pk=id)
        movie_instance.delete()
        return None

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()

class Mutation(AuthMutation, graphene.ObjectType):
    create_Movie = CreateMovie.Field()
    update_Movie = UpdateMovie.Field()
    delete_Movie = DeleteMovie.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
