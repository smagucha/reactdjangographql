import React from 'react';
import {useQuery, gql} from "@apollo/client";
import { Link } from "react-router-dom";
import './static/css/table.css'

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
  const { data, loading, error } = useQuery(
    QUERY_MOVIES, {
      pollInterval: 500 // refetch the result every 0.5 second
    }
  );
  // should handle loading status
  if (loading) return <p>Loading...</p>;
  if (error) return <p>something went wrong </p>;
  return (
    <div>
    <Link to="/AddMovie">addmovie</Link>
        <table>
        	<tr>
        		<th>id</th>
        		<th>name</th>
        		<th>description</th>
            <th>update</th>
            <th>delete</th>
        	</tr>
          {data.allMovie.map(movie=>{
            return <tr>
            <td>
            <Link to={`/MovieDetail/${movie.id}`}>
                  {movie.id}
              </Link>
            
            </td>
            <td>{movie.name}</td>
            <td>{movie.description}</td>
            <td>
              <Link to={`/UpdateMovie/${movie.id}`}>
                  update
              </Link>
            </td>
            <td>
               <Link to="/">
                  delete
              </Link>
            </td>
          </tr>
          })}

        </table>      
    </div>
  );
}

export default Home




