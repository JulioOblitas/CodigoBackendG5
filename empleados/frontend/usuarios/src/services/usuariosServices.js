import axios from "axios"

const URL = "http://127.0.0.1:5000/listausuarios"
const URLELIM = "http://127.0.0.1:5000/eliminaruser"

const crearUsuario  = async (nuevoUsuario) =>{
 try {

    const headers  ={
        "Content-Type" : "application/json"
    }
    const  {data} = await axios.post(URL,nuevoUsuario,{headers});
      return data 
 } catch (error) {
     throw error;
 }
}

const eliminarUsuario  = async (id) => {
    try {                
         await axios.delete(`${URLELIM}/${id}`);
            return "Eliminar Usuario";
    } catch (error) {
        throw error;
    }
}

const editarUsuarioPorId  = async (id, objUsuario )  => {
    
    try {
        const headers = {
            "Content-Type": "application/json"        
        }
        
         await axios.put(`${URL}/${id}`, objUsuario, { headers })
            return;
    } catch (error) {
        throw error
    }
}
    const obtenerUsuarios = async () => {
    
        try {
            
            const  {data} = await axios.get(URL);
            return data;
        } catch (error) {
            throw error;
        }
    }

    const obtenerUsuarioPorId  = async (id) => {
        alert("hola3")
        try {
            
            const {data} = await axios.get(`${URL}/${id}`)
                return data;
        } catch (error) {
            throw error
        }
    }



export { crearUsuario, obtenerUsuarios , eliminarUsuario,obtenerUsuarioPorId,editarUsuarioPorId};