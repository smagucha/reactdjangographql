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
	  mutation deleteMovie($id: ID!) {
	    deleteMovie(id: $id){
	    	Movie{
	    		id
	    	}
	    }
	  }
	`;
	const {data, error, loading} =useQuery(QUERY_MOVIES,{ variables: { id } })
	const [deleteMovie] = useMutation(DELETE_MOVIE);
	if (loading) return <p>Loading...</p>;
	if (error) return <p>something went wrong </p>;
	 const removeMovie = (id) => {
		deleteMovie({
		  variables: {
		    id: id,
		  },
		});
		};
	return (
		<div>
		<form action="/">
          <p>{data.movieById.name}</p>
          <p> {data.movieById.description}</p>
          <button onClick={() => removeMovie(data.movieById.id)}> Delete it </button>
        </form>      
		</div>
	)
}

export default DEleteMovie


         





