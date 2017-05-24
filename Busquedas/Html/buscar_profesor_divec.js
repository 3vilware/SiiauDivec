$(document).ready(function(){
  console.log("Script cargado!!!")
  $("#boton_nombre").click(function(){
      console.log("click!1.0")
      $("#resultado").find("tr:gt(0)").remove();
      $.ajax({
          url: "http://localhost:5000/buscar_profesor_nombre",
          data: $("#nombre").serialize(),
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
    fila += "<td>" + valor["nombre"] + "</td>"
    fila += "<td>" + valor["salario"] + "</td>"
    fila += "<td>" + valor["puesto"] + "</td>"
    fila += "<td>" + valor["carrera"] + "</td>"
    fila += "<tr>"
    $("#resultado").append(fila)
  })
}