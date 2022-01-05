
import { useState, useEffect, useRef } from "react";
import { obtenerUsuarios } from "../services/usuariosServices"
import { Link } from "react-router-dom"
import "../css/estilos.css"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ListaUsuariosView from "../views/ListaUsuariosView"
export default function Formusuario({ value, actualizarInput, manejarSubmit, manejarImagen, valueotro }) {

const [usuarios, setUsuarios] = useState([])  

const [imagen, setImagen] = useState(null);

const [cargadoimg, setCargadoImg] = useState(false);


const getUsuarios = async() =>{

    try {
        
        const usuariosobtenidos  = await obtenerUsuarios()

        setUsuarios (usuariosobtenidos); // despues que obtenemos los datos actualizamos el estado

      
    } catch (error) {
        console.log(error);
        
    }
};


  
  useEffect(() =>{
      getUsuarios();
  },[]);

  const inputfile  = useRef();

  
  
  function VerImagen  (e)  {

    if ( e.target.files && e.target.files[0]){ 
    
    
        let reader = new FileReader();
    
    reader.onload = function(e) {
        setImagen(e.target.result);
        
        setCargadoImg(true)
    }   
    reader.readAsDataURL(e.target.files[0])
  
    
 }
}
   

  
    return (
        
        
             
        
        
        <div className = "contenedor">
               <div className = "principalcategorias">

               
            {/*console.log({valueotro})*/}
            
            <h1> MANTENIMIENTO DE USUARIOS</h1>
            <br />

            <form onSubmit = {(e) => {manejarSubmit(e)}}>
                
                 <div className = "mb-3">

                    <label className = "form-label labelalinear">
                        Dni
                    </label>    
                    <input type="text" className = "cajastextodni" name = "dni" value = {value.dni} onChange ={(e)=> {actualizarInput(e)}}/>
                </div>
                <div className = "mb-3">
                <label className = "form-label labelalinear">
                    Apellidos
                </label>
                   
                <input type="text" className = "cajastextoapellidos" name = "apellidos" value = {value.apellidos} onChange ={(e)=> {actualizarInput(e)}}/>
                 </div>

                 <div className = "mb-3">
                     
                    <label className = "form-label labelalinear">
                        Nombres
                    </label>
                     <input type="text" className = "cajastextonombres"  name = "nombres" value = {value.nombres} onChange ={(e)=> {actualizarInput(e)}}
                      />
                 </div>
                 
                 <div className = "mb-3">
                     
                    <label className = "form-label labelalinear">
                       Area
                    </label>
                     <input type="text" className = "cajastextoarea"  name = "area" value = {value.area} onChange ={(e)=> {actualizarInput(e)}}
                      />
                 </div>

                                  
                 <button className = "btn btn-primary me-2 labelalinear" type = "submit">GUARDAR</button>
                 
                        <Link to ="/listaruser" className = "btn btn-primary">
                            LISTAR - ACTUALIZAR - ELIMINAR  USUARIOS
                         </Link>
                         {
                         <Routes>
                            <Route path = "/listaruser" element ={<ListaUsuariosView  />}/>    
              
                        </Routes>
                        }
                             
            </form>
                
            </div>
          </div>
    )
}
