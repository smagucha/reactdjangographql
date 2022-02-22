import { Outlet, Link } from "react-router-dom";
function Nav(){
	return(
		<>
      <nav>
        <ul>
          <li>
            <Link to="/">Homepage</Link>
          </li>
          <li>
            <Link to="/AddMovie">AddMovie</Link>
          </li>
           <li>
            <Link to="/Login">Login</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
		)
}

export default Nav



