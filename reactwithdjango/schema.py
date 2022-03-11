import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
import graphql_jwt


from django.contrib.auth.models import User
from rctdj.models import Movie, Buses,Routes, Ticket



class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = '__all__'

class CusType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class BusesType(DjangoObjectType):
    class Meta:
        model = Buses
        fields = '__all__'

class TicketType(DjangoObjectType):
    class Meta:
        model = Ticket
        fields ='__all__'

class RouteType(DjangoObjectType):
    class Meta:
        model = Routes
        fields ='__all__'




class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_movie = graphene.List(MovieType)
    movie_by_id = graphene.Field(MovieType, id=graphene.ID())
    all_buses = graphene.List(BusesType)
    buses_by_id =graphene.Field(BusesType, id = graphene.ID())
    # movie_by_name = graphene.Field(MovieType, movie_id=graphene.Int())
    all_ticket = graphene.List(TicketType)
    all_routes = graphene.List(RouteType)

    def resolve_all_ticket(root, info):
        return Ticket.objects.all()

    def resolve_all_movie(root, info):
    	return Movie.objects.all()

    def resolve_all_routes(root, info):
        return Routes.objects.all()

    def resolve_movie_by_id(root, info, id):
    	try:
    		return Movie.objects.get(id=id)
    	except Movie.DoesNotExist:
    		return None

    def resolve_all_buses(root, info):
        return Buses.objects.all()

    def resolve_buses_by_id(root, info, id):
        try:
            return Buses.objects.get(id=id)
        except Buses.DoesNotExist:
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
class createRoute(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    From = graphene.String()
    To = graphene.String()

    class Arguments:
        name = graphene.String()
        From = graphene.String()
        To = graphene.String()

    def mutate(self,info, name, From, To):
        route= Routes(name=name, From=From, To=To)
        route.save()
        return createRoute(id=route.id, name=route.name, From=route.From, To=route.To)

class Createbus(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    seat= graphene.Int()

    class Arguments:
        name = graphene.String()
        seat = graphene.Int()

    def mutate(self, info, name, seat):
        bus = Buses(name = name, seat=seat)
        bus.save()
        return Createbus(
            id = bus.id,
            name= bus.name,
            seat = bus.seat
            )
class UpdateBus(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    seat= graphene.Int()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        seat = graphene.Int()
    bus = graphene.Field(BusesType)
    
    @staticmethod
    def mutate(root, info, id, name, seat):

        bus = Buses.objects.get(pk=id)
        bus.name = name
        bus.seat = seat
        bus.save()
        
        return UpdateBus(bus=bus)
class DeleteBus(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    bus = graphene.Field(BusesType)
    @staticmethod
    def mutate(root, info, id):
        bus_instance = Buses.objects.get(pk= id)
        bus_instance.delete()
        return None 

# class DeleteMovie(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()

#     Movie = graphene.Field(MovieType)

#     @staticmethod
#     def mutate(root, info, id):
#         movie_instance = Movie.objects.get(pk=id)
#         movie_instance.delete()
#         return None


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
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()



class Mutation(AuthMutation, graphene.ObjectType):
    create_route= createRoute.Field()
    create_bus = Createbus.Field()
    update_bus = UpdateBus.Field()
    delete_bus = DeleteBus.Field()
    create_Movie = CreateMovie.Field()
    update_Movie = UpdateMovie.Field()
    delete_Movie = DeleteMovie.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)



# create
# mutation{
#   createCustomer(firstname: "Daniela", lastname:"mokobi", phone:"07521811264"
#   , email:"danielmokobi",IDNumber:405487, cus:2){
#     customer{
#       firstname,
#       lastname,
#       phone,
#       email,
#       cus{
#         id,
#         username,
#       }
     
      
#     }
#   }
# }

################### or #############################
#