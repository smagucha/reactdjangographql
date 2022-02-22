import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
import graphql_jwt


from django.contrib.auth.models import User
from rctdj.models import Movie, Buses, Customer, Routes, Ticket



class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = '__all__'

class CusType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'

class BusesType(DjangoObjectType):
    class Meta:
        model = Buses
        fields = '__all__'


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_movie = graphene.List(MovieType)
    all_customer = graphene.List(CustomerType)
    customer_by_id = graphene.Field(CustomerType, id =graphene.ID())
    movie_by_name = graphene.Field(MovieType, name=graphene.String(required=True))
    all_buses = graphene.List(BusesType)
    buses_by_id =graphene.Field(BusesType, id = graphene.ID())
    # movie_by_name = graphene.Field(MovieType, movie_id=graphene.Int())

    def resolve_all_movie(root, info):
    	return Movie.objects.all()

    def resolve_movie_by_name(root, info, name):
    	try:
    		return Movie.objects.get(name=name)
    	except Movie.DoesNotExist:
    		return None

    def resolve_all_customer(root, info):
        return Customer.objects.all()

    def resolve_customer_by_id(root, info, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
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


class CreateCustomer(graphene.Mutation):
   

    class Arguments:
        firstname = graphene.String()
        lastname = graphene.String()
        IDNumber = graphene.Int()
        phone = graphene.String()
        email = graphene.String()
        cus = graphene.ID()
    customer = graphene.Field(CustomerType)
    

    def mutate(self, info, firstname= None, lastname = None, IDNumber = None, phone=None, email=None, cus=None):
        customer = Customer.objects.create(
            firstname=firstname,
            lastname = lastname,
            IDNumber = IDNumber, 
            phone=phone, 
            email=email,
            cus_id= cus,
            )
        customer.save()
        return CreateCustomer(customer=customer)

class UpdateCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        firstname = graphene.String()
        lastname = graphene.String()
        IDNumber = graphene.Int()
        phone = graphene.String()
        email = graphene.String()
        cus = graphene.ID()
    customer = graphene.Field(CustomerType)
    def mutate(self, info, id = None, firstname= None, lastname = None, IDNumber = None, phone=None, email=None, cus=None):

        customer = Customer.objects.get(pk=id)
        customer.firstname = firstname
        customer.lastname = lastname
        customer.IDNumber = IDNumber
        customer.phone = phone
        customer.email = email
        customer.cus_id = cus
        customer.save()
        return UpdateCustomer(customer=customer)

class DeleteCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    Customer = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id):
        customer_instance = Customer.objects.get(pk=id)
        customer_instance.delete()
        return None

        

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()



class Mutation(AuthMutation, graphene.ObjectType):
    create_bus = Createbus.Field()
    update_bus = UpdateBus.Field()
    delete_bus = DeleteBus.Field()
    create_Movie = CreateMovie.Field()
    update_Movie = UpdateMovie.Field()
    delete_Movie = DeleteMovie.Field()
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
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