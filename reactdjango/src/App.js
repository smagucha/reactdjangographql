
import { ApolloClient,ApolloProvider,InMemoryCache} from "@apollo/client";
import Home from './components/Home'
import AddMovie from './components/AddMovie'
 function App() {
   const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/', // your GraphQL Server 
  cache: new InMemoryCache()
});
   console.log(client)
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
       <h2>My first Apollo app <span role="img" aria-label="rocket">🚀</span></h2>
       <Home/>
       <AddMovie/>
      </div>
   </ApolloProvider>
  );
}
 export default App


