
import React from 'react';
import { useMutation, gql } from '@apollo/client';

function AddMovie() {
 

  const CREATE_MOVIE = gql`
	mutation createMovie ($name: String!, $description: String!){
		createMovie (name: $name, description: $description){
		  id
		  name
		  description
		}
	}
	`;

  const [name, setName] = React.useState("");
  const [description, setDescription] = React.useState("");
  const [createMOVIE, { loading, error }] = useMutation(CREATE_MOVIE);

  function handleCreateMovie(event) {
    event.preventDefault();
    // the mutate function also doesn't return a promise
    createMOVIE({ variables: { name, description } });
  }

  return (
    <div>
      <h1>New Movies</h1>
      <form onSubmit={handleCreateMovie}>
        <input onChange={(event) => setName(event.target.value)} />
        <input onChange={(event) => setDescription(event.target.value)} />
        <button disabled={loading} type="submit">
          Submit
        </button>
        {error && <p>{error.message}</p>}
      </form>
    </div>
  );
}
export default AddMovie


