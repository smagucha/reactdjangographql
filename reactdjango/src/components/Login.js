import React from 'react'

function Login(){
	return (
		<div>
		<p>
			<label htmlFor="username">
				username
			</label>
			<input type="text" name='username'/>
		</p>
		<p>
			<label htmlFor="password">
				password
			</label>
			<input type="password" name='password'/>
		</p>
			<button>
				login
			</button>
		</div>
	)
}
export default Login