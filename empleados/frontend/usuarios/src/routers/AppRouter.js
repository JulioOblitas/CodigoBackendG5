import  {BrowserRouter ,  Route, Routes } from "react-router-dom";

import CrearUsuariosView from "../views/CrearUsuariosView"
import ListaUsuariosView from "../views/ListaUsuariosView"

export default function AppRouter() {
    return (        
        <BrowserRouter>  
          <Routes>
            <Route path="/crearusuario" element={<CrearUsuariosView />} />
            <Route path="/listaruser" element={<ListaUsuariosView />} />

            
        </Routes>          
        </BrowserRouter>                    
        
    );
}
