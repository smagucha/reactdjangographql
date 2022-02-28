import React from 'react';
import { useState } from "react";
import './static/css/form.css'
import {useQuery, gql, useMutation} from "@apollo/client";
import { useParams} from "react-router"
function UpdateMovie() {
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
    const UPDATE_MOVIE = gql`
        mutation updateMovie($id:Int, $name: String, $description: String){
          updateMovie(id:$id, name:$name, description:$description){
            movie{
              id
              name
              description          
            }
          }
      }
    `;

  const {data} =useQuery(QUERY_MOVIES,{ variables: { id } })
  const [name, setName] = useState(data.movieById.name);
  const [description, setDescription] = useState(data.movieById.description);
  const [updateMOVIE, {error }] = useMutation(UPDATE_MOVIE);
  
  function handleUpdateMovie(event) {
    event.preventDefault();
    updateMOVIE({ variables: { id, name, description } });
  }

    return (
    <div>
      <form onSubmit={handleUpdateMovie} action="/">
        <input type="text"  defaultValue={data.movieById.name} onChange={(event) => setName(event.target.value)} />
        <input type="text" defaultValue={data.movieById.description} onChange={(event) => setDescription(event.target.value)} />
        <button type="submit">
          Submit
        </button>
        
        {error && <p>{error.message}</p>}
      </form>
    </div>
  );
}

export default UpdateMovie




