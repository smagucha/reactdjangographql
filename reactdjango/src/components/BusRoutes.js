import {useQuery, gql} from "@apollo/client";
import {Link} from "react-router-dom";

const QUERY_ROUTES = gql`
query{
  allRoutes{
    id,
    name,
    From,
    To
    
  }
}
`;
function BusRoutes(){
const { data, loading, error } = useQuery(
   QUERY_ROUTES, {
      pollInterval: 500 // refetch the result every 0.5 second
    }
  );
  // should handle loading status
  if (loading) return <p>Loading...</p>;
  if (error) return <p>something went wrong </p>;


	return(
		<div>
		<h1>Hello LIST routes</h1>
		<Link to="/AddRoute">Add routes</Link>
			<table>
        	<tr>
        		<th>name</th>
        		<th>From</th>
        		<th>To</th>
        		<th>delete</th>
        	</tr>
          {data.allRoutes.map(road=>{
            return <tr>
            <td>{road.name}</td>
            <td>{road.From}</td>
            <td>{road.To}</td>
            <td>
            
            	<Link to={`/DeleteRoute/${road.id}`}>
                  delete
              </Link>
            </td>
          </tr>
          })}

        </table>  
		</div>

		)
}

export default BusRoutes