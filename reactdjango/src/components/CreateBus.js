import React from 'react'
import { useState } from "react";
import { useMutation, gql } from '@apollo/client';
import './static/css/form.css'

export default function CreateBus() {
	const CREATE_BUS = gql`
	mutation createBus ($name: String!, $seat: Int!){
		createBus (name: $name, seat: $seat){
		  id
		  name
		  seat
		}
	}
	`;

  const [name, setName] = useState("");
  const [seat, setSeat] = useState("");
  const [createBUS, {error}] = useMutation(CREATE_BUS);

  function handleCreateBUS(event) {
    createBUS({ variables: { name, seat } });
    event.preventDefault();
    clearState();
  }
  const clearState = () => {
    setName('');
    setSeat('');
  };
	return (
		<div>
	<h1>Create BUS</h1>
	<form onSubmit={handleCreateBUS}>
		<input type="text" onChange={(event) => setName(event.target.value)} />
		<input type="text" onChange={(event) => setSeat(event.target.value)} />
		<button type="submit">
			Submit
		</button>
	{error && <p>{error.message}</p>}
	</form>
		</div>
	)
}