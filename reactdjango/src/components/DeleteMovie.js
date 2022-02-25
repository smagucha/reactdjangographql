import React from 'react'
import {useMutation, gql, useQuery} from '@apollo/client'
import { useParams} from "react-router"



function DEleteMovie() {
	const { id } = useParams();
	const QUERY_MOVIES = gql`
		query{
			movieById(id:${id}){
				id,
				name,
				description
			}
			}
			 `;
	const DELETE_MOVIE = gql`
	  mutation deleteTodo(
	    $id: ID!
	  ) {
	    deleteMovie(
	      id: $id
	    ) {
	      id
	    }
	  }
	`;
	const {data, error, loading} =useQuery(QUERY_MOVIES,{ variables: { id } })
	if (loading) return <p>Loading...</p>;
	if (error) return <p>something went wrong </p>;
	return (
		<div>
		<form action="/">
          <p>{data.movieById.name}</p>
          <p> {data.movieById.description}</p>
          <button>delete</button>
        </form>      
		</div>
	)
}

export default DEleteMovie


         





