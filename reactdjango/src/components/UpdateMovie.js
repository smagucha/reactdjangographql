import React from 'react';
import { useState } from "react";
import './static/css/form.css'
import {useQuery, gql} from "@apollo/client";
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
  const {data, error, loading} =useQuery(QUERY_MOVIES,{ variables: { id } })
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  
  function handleCreateMovie(event) {
    event.preventDefault();
  }

    return (
    <div>
      <h1>New Movies</h1>
      <form onSubmit={handleCreateMovie}>
        <input type="text"  defaultValue={data.movieById.name} onChange={(event) => setName(event.target.value)} />
        <input type="text" defaultValue={data.movieById.description} onChange={(event) => setDescription(event.target.value)} />
        <button  type="submit">
          Submit
        </button>
        {error && <p>{error.message}</p>}
      </form>
    </div>
  );
}

export default UpdateMovie