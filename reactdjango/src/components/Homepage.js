import { ApolloClient,ApolloProvider,InMemoryCache} from "@apollo/client";
import Nav from './Nav'


 function Homepage() {
   const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/', // your GraphQL Server 
  cache: new InMemoryCache()
});
  return (
    <ApolloProvider client={client}>
     <div>
      <Nav/>
      </div>
   </ApolloProvider>
  );
}
 export default Homepage


