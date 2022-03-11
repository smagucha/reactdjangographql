import { Outlet, Link } from "react-router-dom";
import './static/css/nav.css'
function Nav(){
	return(
		<>
      <nav>
        <ul>
          <li>
            <Link className="active" to="/">Home</Link>
          </li>
          <li>
            <Link to="/Ticket">Ticket</Link>
          </li>
           <li>
            <Link to="/ListBus">Buses</Link>
          </li>
           <li>
            <Link to="/BusRoutes">Routes</Link>
          </li>
           <li>
            <Link to="/Customer">Customer</Link>
          </li>
           <li>
            <Link to="/Login">Login</Link>
          </li>
          <li style={{float: "right"}}>
            <Link  to="/Login" >Logout</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
		)
}

export default Nav



