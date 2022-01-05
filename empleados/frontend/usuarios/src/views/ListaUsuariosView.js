import {  useState, useEffect  } from "react";
import { obtenerUsuarios, eliminarUsuario } from "../services/usuariosServices"
import Cargando from "../components/Cargando";
import { Link } from "react-router-dom";

import Swal from "sweetalert2";
export default function ListaUsuariosView() {
    const [usuarios,SetUsuarios] = useState([])
    const [loading,SetLoading] = useState(false) 

    const getUsuarios = async() =>{

        try {
            SetLoading(true)
            const  usuariosobtenidos = await obtenerUsuarios();
            SetUsuarios(usuariosobtenidos);
            SetLoading(false);    
        } catch (error) {
            console.log(error);
        }

        
    };
   
    const verificarEliminar = async(id) => {
        const rpta  = await Swal.fire({
        icon : 'success',
        title : 'Desea Eliminar Categoria',
        text : 'Esta accion es irreversible',
        showConfirmButton: true,
        showDenyButton:true,
        confirmButtonText:"Si, Eliminar",
        denyButtonText:"No, cancelar",
    });

        if (rpta.isConfirmed){
            try {
                await eliminarUsuario(id);

                await Swal.fire({
                    icon : "success",
                    title : "Usuario Eliminado",
                    text :  "Accion de Eliminar Categoria"
                })

                getUsuarios();
                
            } catch (error) {
                    console.log(error);
            }
        }

};



    useEffect(() =>{
        getUsuarios();
    },[]);


    return (
        <>
            {loading ? (
                <Cargando />
            ) : (
                
                <div className = "contenedor"> 
            
                <div className="principalcategorias">
                
                <h1 className = "mb-3">LISTADO DE USUARIOS</h1>
        

                 

                 <table className = "table"> 

                 <thead>
                     <tr>
                         <th>DNI</th>                         
                         <th>APELLIDOS </th>
                         <th>NOMBRES </th>
                         <th>AREA </th>
                         <th>MODIFICAR</th>
                        <th>ELIMINAR</th>
                     </tr>

                 </thead>
                 <tbody>
                     {
                         usuarios.map((userreg,i) =>(
                             <tr key={i}>
                                 <td>{userreg.dni} </td>
                                 <td>{userreg.apellidos} </td>
                                 <td>{userreg.nombres} </td>
                                 <td>{userreg.area} </td>
                                 <td>
                                 <Link  className= "btn btn-info me-2" to ={`/editarusuario/${userreg.dni}`}>  <i className="fas fa-edit"></i> </Link>
                                 </td>                                                    
                                 <td>
                                    <button className = "btn btn-danger" onClick={() => {verificarEliminar(userreg.dni)}}>  <i className="fas fa-eraser"></i>  </button>
                                </td>                                                    
                             </tr>                         
                         ))                         
                     }
                            
                           
                 </tbody>
                 </table>
                 
                 </div>

                 </div>
            )}
            </>
    
    );
}
