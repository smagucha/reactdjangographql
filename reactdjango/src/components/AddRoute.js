import React from 'react'
import { useState } from "react"
import { useMutation, gql } from '@apollo/client'
import './static/css/form.css'

const CREATE_ROUTE = gql`
mutation createRoute ($name: String!, $From: String!,$To: String!){
	createRoute (name: $name, From: $From, To:$To){
	  id,
	  name,
	  From,
	  To
	}
}`

export default function AddRoute() {
	const [name, setName] = useState("")
	const [From, setFrom] = useState("")
	const [To, setTo] = useState("")
	const [createRoute, { loading, error }] = useMutation(CREATE_ROUTE)

	function handleCreateRoad(event) {
	    createRoute({ variables: { name, From, To} });
	    event.preventDefault();
  }
	return (
		<div>
		<h1>add road sam</h1>
      	<form onSubmit={handleCreateRoad}>
      		<label >name</label>
        	<input type="text" onChange={(event) => setName(event.target.value)} />
        	<label >From</label>
        	<input type="text" onChange={(event) => setFrom(event.target.value)} />
        	<label >To</label>
        	<input type="text" onChange={(event) => setTo(event.target.value)} />
        	<button disabled={loading} type="submit">
          		Submit
        	</button>
        	{error && <p>{error.message}</p>}
      </form>			
		</div>
	)
}