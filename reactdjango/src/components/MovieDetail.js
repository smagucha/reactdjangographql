import {useQuery, gql} from "@apollo/client";
import { useParams} from "react-router"
import React from 'react'

function MovieDetail() {
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
	const {data, error, loading} =useQuery(QUERY_MOVIES,{ variables: { id } })
	if (loading) return <p>Loading...</p>;
	if (error) return <p>something went wrong </p>;
	return (
		<div>
          <p>{data.movieById.name}</p>
          <p> {data.movieById.description}</p>      
		</div>
	)
}

export default MovieDetail

         





