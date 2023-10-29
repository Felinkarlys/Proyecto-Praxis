let dataTable;
let dataTableIsInitialized= false; 

const dataTableOp={
    colimnDefs:[
        {className: "centere", targets:[0,1,2,3,4,5,6]},
        {orderable: false,targest: [5]},
        {searchable:false, targets:[0,6]}
    ]
    };



const inidDataTable = async()=>{
if(dataTableIsInitialized){
    dataTable.destroy();
}
await listaHoleken(); 

dataTable=$('#dataTable-holken').DataTable({dataTableOp});

    dataTableIsInitialized= true;
};

const listaHoleken = async () =>{
try { 
    const response = await fetch("http://127.0.0.1:8000/juego/lista_holken/");
    const data = await response.json();

    let content= '';
    let num_holkenArray = [];
    let puntosArray = [];


    data.holken.forEach((holken, index) => {
        content +=`
            <tr>
            <td>${index+1}</td>
            <td>${holken.num_holken}</td>
            <td>${holken.nombre_holken}</td>
            <td>${holken.equipo}</td>
            <td>${holken.rol}</td>
            <td>${holken.puntos}</td>
            <td>${holken.avatar}</td>

            </tr>
      `;
    });

    const tablaBody_holken = document.getElementById('tablaBody_holken'); // Asegúrate de que coincida con el ID en tu HTML.
    tablaBody_holken.innerHTML = content;

     // Llama a la función para graficar los datos
     graficarDatos(num_holkenArray, puntosArray);
    
    
} catch (ex) {
    alert(ex)
    
}

};

window.addEventListener('load', async () => {
await inidDataTable();

});


document.getElementById("backButton").addEventListener("click", function() {
    window.history.back(); // Esta línea regresará a la página anterior en la historia del navegador.
});

// buscar valor


// graficar

function graficarDatos(num_holkenArray, puntosArray) {
    var ctx = document.getElementById("graficoPuntos").getContext("2d");
    var chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: num_holkenArray,  // Usar los números de holken como etiquetas
            datasets: [
                {
                    label: "Puntos",
                    data: puntosArray,  // Usar los puntos como datos
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}