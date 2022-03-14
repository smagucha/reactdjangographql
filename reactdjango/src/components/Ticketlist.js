import React from 'react'
import {useQuery, gql} from "@apollo/client";
import { Link } from "react-router-dom";

const QUERY_Ticket= gql`
 query{
  allTicket{
    firstname,
    lastname,
    phone,
    routes{
      name
    }
    departureTime,
    seat
  }
}
`;
function Ticketlist() {
	const { data, loading, error } = useQuery(
	   QUERY_Ticket, {
	      pollInterval: 500 // refetch the result every 0.5 second
	    }
	  );
	if (loading) return <p>Loading...</p>;
  	if (error) return <p>something went wrong </p>;
  	console.log({data})
	return (
		<div>
		<Link to="/AddMovie">addmovie</Link>
			<table>
        	<tr>
	        	<th>firstname</th>
	        	<th>lastname</th>
	            <th>phone</th>
	            <th>routes</th>
	            <th>departure time</th>
	            <th>seat</th>
	            <th>update</th>
	            <th>delete</th>
        	</tr>

          {data.allTicket.map(ticket=>{
            return <tr>
            <td>{ticket.firstname}</td>
            <td>{ticket.lastname}</td>
            <td>{ticket.phone}</td>
            <td>{ticket.routes.name}</td>
            <td>{ticket.departureTime}</td>
            <td>{ticket.seat}</td>
            <td>
              <Link to="/AddMovie">
                  update
              </Link>
            </td>
            <td>
               <Link to="/AddMovie">
                  delete
              </Link>
              </td>
          </tr>
          } ) }

        </table> 
			
		</div>
	)
}

export default Ticketlist