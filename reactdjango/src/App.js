import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './components/Home'
import AddMovie from './components/AddMovie'
import Homepage from './components/Homepage'
import Login from './components/Login'
import UpdateMovie from './components/UpdateMovie'
import MovieDetail from './components/MovieDetail'
import DeleteMovie from './components/DeleteMovie'
import CreateBus from './components/CreateBus'
import ListBus from './components/ListBus'

 function App() {
  return (
     <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />}>
          <Route index element={<Home />} />
          <Route path="/AddMovie" element={<AddMovie />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/UpdateMovie/:id" element={<UpdateMovie />} />
          <Route path="/DeleteMovie/:id" element={<DeleteMovie />} />
          <Route path ='/MovieDetail/:id' element={<MovieDetail />} />
          <Route path = '/CreateBus' element={<CreateBus/>}/>
          <Route path='/ListBus' element={<ListBus/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
 export default App


