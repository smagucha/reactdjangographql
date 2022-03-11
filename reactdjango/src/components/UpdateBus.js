import { useState } from "react";
import { useParams} from "react-router"
import {useQuery, gql, useMutation} from "@apollo/client";


function UpdateBus() {
	
	const { id } = useParams();
	const QUERY_BUS = gql`
	query{
 		busesById(id:3){
    	id,
    	name,
    	seat
	  }
	}
	   `;
	const UPDATE_BUS = gql`
        mutation updateBus($id:Int, $name: String, $seat: Int){
          updateBus(id:$id, name:$name, seat:$seat){
            bus{
              id
              name
              seat         
            }
          }
      }
    `;
   
	const {data} =useQuery(QUERY_BUS,{ variables: { id } })
	const [name, setName] = useState(data.busesById.name);
	const [seat, setSeat] = useState(data.busesById.seat);
	const [updateBus, {error }] = useMutation(UPDATE_BUS);
	function handleUpdateBus(event) {
    	event.preventDefault();
	    updateBus({ variables: { id, name, seat} });
	    window.location.href ="/ListBus"
	  }

	return (
		<div>

			<form onSubmit={handleUpdateBus} >
				<p>
					<label htmlFor="name">
						Name
					</label>
					<input type="text" name="name"  defaultValue={data.busesById.name} onChange={(event) => setName(event.target.value)}/>
				</p>
				<p>
					<label htmlFor="seat">
						Seat
					</label>
					<input type="number" name="seat" defaultValue={data.busesById.seat} onChange={(event) => setSeat(event.target.value)}/>
				</p>
				<button type="submit">
					Submit
				</button>
				 {error && <p>{error.message}</p>}
			</form>
		</div>
	)
}

export default UpdateBus