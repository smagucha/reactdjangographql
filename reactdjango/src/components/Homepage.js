import { ApolloClient,ApolloProvider,InMemoryCache} from "@apollo/client";
import Nav from './Nav'


 function Homepage() {
   const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/', // your GraphQL Server 
  cache: new InMemoryCache()
});
  return (
    <ApolloProvider client={client}>
     <div style={{
       backgroundColor: '#00000008',
       display: 'flex',
       justifyContent:'center',
       alignItems:'center',
       height: '100vh',
       flexDirection: 'column',
     }}>
      <Nav/>
       <h2>My first Apollo Homepage <span role="img" aria-label="rocket">🚀</span></h2>
      </div>
   </ApolloProvider>
  );
}
 export default Homepage


