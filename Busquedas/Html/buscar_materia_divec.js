$(document).ready(function(){
  console.log("Script cargado!!!")
  $("#boton_buscar").click(function(){
      console.log("click!2.0")
      $("#resultado").find("tr:gt(0)").remove();
      $.ajax({
          url: "http://localhost:5000/buscar_materia_profesor",
          data: $("#form").serialize(),
          type: "POST",
          success: function(respuesta){
            console.log(respuesta)
            mostrar_resultado(respuesta)
          },
          error: function(respuesta){
            console.log(respuesta)
          }
      })
  })
})

function mostrar_resultado(respuesta){
  $.each(respuesta, function(index,valor){
    var fila = "<tr>"
    fila += "<td>" + valor["nrc"] + "</td>"
    fila += "<td>" + valor["nombreProfesor"] + "</td>"
    fila += "<td>" + valor["clave"] + "</td>"
    fila += "<td>" + valor["nombreMateria"] + "</td>"
    fila += "<td>" + valor["seccion"] + "</td>"
    fila += "<td>" + valor["inicio"] + "</td>"
    fila += "<td>" + valor["fin"] + "</td>"
    fila += "<td>" + valor["ciclo"] + "</td>"
    fila += "<tr>"
    $("#resultado").append(fila)
  })
}