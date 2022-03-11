import {Link} from "react-router-dom";
import {useQuery, gql} from "@apollo/client";

const QUERY_BUSES = gql`
 query{
  allBuses{
    id,
    name,
    seat,
  }
}
`;

function ListBus() {
	const { data, loading, error } = useQuery(
   QUERY_BUSES, {
      pollInterval: 500 // refetch the result every 0.5 second
    }
  );
  // should handle loading status
  if (loading) return <p>Loading...</p>;
  if (error) return <p>something went wrong </p>;
	return (
		<div>

			<Link to="/CreateBus">Add Bus</Link>
			<table>
        	<tr>
        		<th>name</th>
        		<th>seat</th>
            <th>update</th>
            <th>delete</th>
        	</tr>
          {data.allBuses.map(bus=>{
            return <tr>
            <td>{bus.name}</td>
            <td>{bus.seat}</td>
            <td>
              <Link to={`/UpdateBus/${bus.id}`}>
                 update
              </Link>
            </td>
            <td>
               <Link to={`/Deletebus/${bus.id}`}>
                  delete
              </Link>
            </td>
          </tr>
          })}

        </table>  
		</div>
	)
}

export default  ListBus