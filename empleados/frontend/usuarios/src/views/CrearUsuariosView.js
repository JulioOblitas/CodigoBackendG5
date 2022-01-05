import { useState,  useEffect } from "react"
import { useNavigate } from "react-router-dom";
import { crearUsuario } from "../services/usuariosServices";
import Formusuario from "../components/Formusuario"
import Cargando from "../components/Cargando";
import Swal from "sweetalert2";





let imagen;  //variable global no definida

let imageUrl;
export default function CrearUsuariosView() {
    
    const [value, SetValue] = useState( {
        
    });
    const [valueotro, SetValueotro] = useState(null);
    
    const [loading, SetLoading] = useState(false);

    const navigate  = useNavigate();

const actualizarInput = (e) =>{
    SetValue ({...value,[e.target.name]:e.target.value})  //cogiendo el estado de lvalue y spred operatr
    
};  



const manejarSubmit = async(e) =>{
  e.preventDefault();

  try {
    
    
    SetLoading(true);
    
    await crearUsuario({...value});
    SetLoading(false);
    await Swal.fire({
        icon:'success',
        title:'exito',
        text: 'Usuario Creado',
        showConfirmButton:false,
        timer: 2000,

    })
    navigate("/");
  } catch (error) {
        console.log(error);
  }
  
  
  //console.log("submit ejecutaod")
};

    const manejarImagen = (e) => {
        e.preventDefault();
        
        imagen = e.target.files[0];
        imageUrl = URL.createObjectURL(imagen)
        SetValueotro (imageUrl)  //cogiendo el estado de lvalue y spred operatr  
                
          

        
        //console.log(e.target.files[0]);
        
     
    };
    
    
    useEffect(()=>{
    }, []);
    

    return (
        
        <>
        
        
            {loading === true ? (
                <Cargando />
            ) : (
                <Formusuario value = {value} actualizarInput = {actualizarInput} manejarSubmit = {manejarSubmit}  manejarImagen = {manejarImagen} valueotro = {valueotro} />                       
            )}          
        </>
    );
}
