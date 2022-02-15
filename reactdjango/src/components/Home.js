import React from 'react';
import {useQuery, gql} from "@apollo/client";
const QUERY_MOVIES = gql`
  query{
	allMovie{
	  id
	  name
	  description
	}
}
`;
function Home() {
  const { data, loading } = useQuery(
    QUERY_MOVIES, {
      pollInterval: 500 // refetch the result every 0.5 second
    }
  );
  // should handle loading status
  if (loading) return <p>Loading...</p>;
   
  return data.allMovie.map(({ id, name, description }) => (
    <div>
        <table>
        	<tr>
        		<th>id</th>
        		<th>name</th>
        		<th>description</th>
        	</tr>
        	<tr>
        		<td>{id}</td>
        		<td>{name}</td>
        		<td>{description}</td>
        	</tr>
        </table>

      
    </div>
  ));
}

export default Home





