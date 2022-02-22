import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './components/Home'
import AddMovie from './components/AddMovie'
import Homepage from './components/Homepage'
import Login from './components/Login'

 function App() {
  return (
     <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />}>
          <Route index element={<Home />} />
          <Route path="/AddMovie" element={<AddMovie />} />
          <Route path="/Login" element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
 export default App


