
var nombre=document.getElementById("nombre");
var rut=document.getElementById("rut");
var contraseña = document.getElementById("contraseña");
var rep_contraseña = document.getElementById("rep_contraseña");
var email=document.getElementById("email");
var mod=document.getElementById("mod");
var detalles = document.getElementById("detalles");
var error = document.getElementById("error");


function enviar(){
    console.log("enviando datos desde js");
    var mensaje=[];
     
    if(nombre.value===null || nombre.value==""){
        mensaje.push("Debe ingresar un nombre");
    }
    
    if(rut.value===null || rut.value==""){
        mensaje.push("Debe ingresar un rut");
    }
    
    if(contraseña.value===null || contraseña.value==""){
        mensaje.push("Debe ingresar una contraseña");
        
    }
    
    if(rep_contraseña.value===null || rep_contraseña.value==""){
        mensaje.push("Debe repetir la contraseña");
    }
    if (contraseña.value !== rep_contraseña.value) {
        mensaje.push("Las contraseñas no coinciden");
      }
    
    if(email.value===null || email.value==""){
        mensaje.push("Debe ingresar un correo");
    }
    
    if (mod.value===null || mod.value==""){
        mensaje.push("Debe ingresar una region");
    }
    if(detalles.value===null || detalles.value==""){
        mensaje.push("Debe ingresar un detalle");
    }
    
    if (mensaje.length === 0) {

        error.innerHTML = "Enviado";
      } else {
        error.innerHTML = mensaje.join(", ");
      };


    return false;
}

function mostrarTexto() {
  var parrafo = document.getElementById("parrafo");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}
function mostrarTexto2() {
  var parrafo = document.getElementById("parrafo2");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}
function mostrarTexto3() {
  var parrafo = document.getElementById("parrafo3");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}
function mostrarTexto4() {
  var parrafo = document.getElementById("parrafo4");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}
function mostrarTexto5() {
  var parrafo = document.getElementById("parrafo5");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}
function mostrarTexto6() {
  var parrafo = document.getElementById("parrafo6");
  if (parrafo.style.display === "none") {
    parrafo.style.display = "block";
  } else {
    parrafo.style.display = "none";
  }
}

