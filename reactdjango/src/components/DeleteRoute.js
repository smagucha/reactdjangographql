import React from 'react'
import {useMutation, gql, useQuery} from '@apollo/client'
import { useParams} from "react-router"

function DeleteRoute() {
	const { id } = useParams();
	const QUERY_ROUTE = gql`
		query{
		  routeById(id:${id}){
		    id,
		    name,
		    To,
		    From
		  }
		}
			 `;
	const DELETE_ROUTE = gql`
	  mutation deleteRoute($id: ID!) {
	    deleteRoute(id: $id){
	    	route{
	    		id
	    		name
	    		From
	    		To
	    	}
	    }
	  }	
	  `;
	const {data, error, loading} =useQuery( QUERY_ROUTE,{ variables: { id } })
	const [deleteRoute] = useMutation(DELETE_ROUTE);
	if (loading) return <p>Loading...</p>;
	if (error) return <p>something went wrong </p>;
	 const removeroute = (id) => {
		deleteRoute({
		  variables: {
		    id: id,
		  },
		});
		};
	return (
		<div>
		<h1>helloo delete</h1>
		<form action="/BusRoutes">
         <p>{data.routeById.name}</p>
         <p> {data.routeById.From}</p>
         <p> {data.routeById.To}</p>

          <button onClick={() => removeroute(data.routeById.id)}> Delete it </button>
        </form> 
			
		</div>
	)
}


export default DeleteRoute
